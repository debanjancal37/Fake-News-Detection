
/* static/script.js */

// Select the news input fields and buttons
const newsTitle = document.getElementById("news_title");
const newsText = document.getElementById("news_text");
const charCount = document.getElementById("charCount");
const clearBtn = document.getElementById("clearBtn");
const newsForm = document.getElementById("newsForm");

// Update the article character count
function updateCharCount() {
    const totalCharacters = newsText.value.length;
    charCount.textContent = `${totalCharacters} characters`;
}

// Update the count whenever the article text changes
newsText.addEventListener("input", updateCharCount);

// Clear the input fields
clearBtn.addEventListener("click", function () {
    newsTitle.value = "";
    newsText.value = "";
    updateCharCount();
    newsTitle.focus();
});

// Display the initial character count
updateCharCount();

// Prevent accidental submission of completely empty fields
newsForm.addEventListener("submit", function (event) {
    if (!newsTitle.value.trim() && !newsText.value.trim()) {
        event.preventDefault();
        alert("Please enter a news title or article text.");
    }
});
