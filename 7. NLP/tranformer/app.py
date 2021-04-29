from flask import Flask, render_template,request
app = Flask(__name__)
from transformers import pipeline

def translate(text):
    translators = pipeline('translation_en_to_de')
    text = translators(text)
    key1, value1 = text[0].items()
    return value1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate',methods=["POST"])
def translatetext():
    if request.method == "POST":
        data = request.form.to_dict()
        print (data)
        key,text = list(data.items())[0]
        print(text)

        translated_text = translate(text)

        return render_template("index.html", response=translated_text)
        

if __name__== "__main__":
    app.run(debug=True)