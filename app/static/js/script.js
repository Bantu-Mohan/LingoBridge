// script.js
document.getElementById('translate-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var text = document.getElementById('input-text').value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'text=' + encodeURIComponent(text)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('original-text').innerText = "Original Text: " + data.original_text;
            document.getElementById('detected-language').innerText = "Detected Language: " + data.detected_language_name + " (" + data.detected_language_code + ")";
            document.getElementById('translated-text').innerText = "Translated Text: " + data.translated_text;
        }
    })
    .catch(error => {
        alert("Translation failed. Please try again.");
    });
});
