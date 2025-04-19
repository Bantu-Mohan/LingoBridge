from flask import Flask, request, jsonify, render_template
from langdetect import detect, DetectorFactory
from googletrans import Translator, LANGUAGES

# Ensure consistent language detection
DetectorFactory.seed = 0

app = Flask(__name__, static_folder="static")

def get_language_full_name(lang_code):
    """Get the full name of a language from its code."""
    return LANGUAGES.get(lang_code, "Unknown").capitalize()

@app.route('/')
def index():
    """Render the index.html page."""
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    """Detect the language of the text, translate it to English, and return details."""
    try:
        text = request.form.get('text')
        detected_lang_code = detect(text)
        detected_lang_name = get_language_full_name(detected_lang_code)

        # Translate the text to English
        translator = Translator()
        translated = translator.translate(text, src=detected_lang_code, dest='en')

        return jsonify({
            "original_text": text,
            "detected_language_code": detected_lang_code,
            "detected_language_name": detected_lang_name,
            "translated_text": translated.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
