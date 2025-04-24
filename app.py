from flask import Flask, render_template, request
from translator import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    text = ""
    lang = "en"
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]
        translated_text = translate_text(text, lang)
    return render_template("index.html", translated_text=translated_text, text=text, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
