

# Fake News Detection using Flask and Linear SVM


from flask import Flask, render_template, request
import joblib
import os

# Initialize Flask application
app = Flask(__name__)

# 1. Define project and model file paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_fake_news_svm_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

# Check whether the model files exist
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

if not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError(
        f"TF-IDF vectorizer not found: {VECTORIZER_PATH}"
    )

# 2. Load the trained model and vectorizer

svm_model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

print("Linear SVM model loaded successfully.")
print("TF-IDF vectorizer loaded successfully.")

# 3. Define explicit fictional-text indicators

FICTIONAL_INDICATORS = [
    "fictional online report",
    "invented news story",
    "this is a fictional story",
    "this story is fictional",
    "completely fictional"
]

# 4. Home page and prediction route


@app.route("/", methods=["GET", "POST"])
def home():

    # Initialize page variables
    prediction = None
    prediction_note = None
    news_title = ""
    news_text = ""
    error = None

    if request.method == "POST":

        # Get user input from the HTML form
        news_title = request.form.get(
            "news_title", ""
        ).strip()

        news_text = request.form.get(
            "news_text", ""
        ).strip()

        # Validate input
        if not news_title and not news_text:

            error = (
                "Please enter a news title "
                "or article text."
            )

        else:

            # Combine title and article text
            combined_news = (
                f"{news_title} {news_text}"
            )

            # Remove extra whitespace
            combined_news = " ".join(
                combined_news.split()
            )

            # Convert text to lowercase for rule checking
            text_lower = combined_news.lower()


            # 5. Check explicit fictional indicators


            contains_fictional_indicator = any(
                phrase in text_lower
                for phrase in FICTIONAL_INDICATORS
            )

            if contains_fictional_indicator:

                # Flag text that explicitly describes itself
                # as fictional or invented.
                prediction = "Fake News"

                prediction_note = (
                    "Flagged because the submitted text "
                    "explicitly identifies itself as fictional. "
                    "This is a rule-based warning, not "
                    "independent fact verification."
                )

            else:

                # 6. Run the trained Linear SVM model


                # Transform the input using the saved vectorizer
                news_features = tfidf.transform(
                    [combined_news]
                )

                # Predict the label
                predicted_label = int(
                    svm_model.predict(news_features)[0]
                )

                # IMPORTANT:
                # This mapping assumes WELFake labels:
                # 0 = Fake, 1 = Real.
                if predicted_label == 0:

                    prediction = "Fake News"

                elif predicted_label == 1:

                    prediction = "Real News"

                else:

                    prediction = (
                        f"Unknown label: {predicted_label}"
                    )

                prediction_note = (
                    "This is a machine-learning prediction. "
                    "It may be incorrect and does not "
                    "independently verify the news."
                )

    # 7. Render the HTML page

    return render_template(
        "index.html",
        prediction=prediction,
        prediction_note=prediction_note,
        news_title=news_title,
        news_text=news_text,
        error=error
    )

# 8. Run the Flask application

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
