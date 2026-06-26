from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

@app.route("/", methods=["GET", "POST"])
def index():

    translated = ""

    if request.method == "POST":

        text = request.form["text"]

        source = request.form["source"]

        target = request.form["target"]

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

    return render_template(
        "index.html",
        languages=languages.keys(),
        translated=translated
    )

if __name__ == "__main__":
    app.run(debug=True)
    