
# Fake News Detection Using Machine Learning

## Project Overview

This project classifies news text as Fake News or Real News
using Natural Language Processing (NLP) and machine learning.

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Linear Support Vector Machine (Linear SVM)
- HTML, CSS and JavaScript

## Models Evaluated

- Multinomial Naive Bayes
- Logistic Regression
- Linear SVM

Linear SVM achieved the highest F1-score of 0.9773
in the recorded test evaluation.

## Features

- News title and article text input
- TF-IDF text transformation
- Machine learning-based classification
- Web interface built with Flask
- Responsive user interface

## Project Structure

```text
Fake-News-Detection/
├── app.py
├── requirements.txt
├── README.md
├── models/
│   ├── best_fake_news_svm_model.pkl
│   └── tfidf_vectorizer.pkl
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Run the Flask application:

   python app.py

5. Open http://127.0.0.1:5000 in your browser.

## Disclaimer

This model produces predictions based on learned text patterns.
It does not independently verify news or guarantee factual accuracy.

## Author 

Debanjan Gayen

Data Analyst | Python | SQL | Power BI | Machine Learning | NLP | RAG
