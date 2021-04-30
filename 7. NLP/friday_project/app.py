from flask import Flask, render_template,request
from transformers import pipeline
import speech_recognition as sr

app = Flask(__name__)


def microphone():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=2)
    with mic as source:
        audio = r.listen(source)
    audio_text = r.recognize_google(audio)
    return audio_text


def speech_to_text(files):
    r = sr.Recognizer()
    harvard = sr.AudioFile(files)
    with harvard as source:
        audio = r.record(source)
    generated_text = r.recognize_google(audio)
    return generated_text


def translate(text):
    translators = pipeline('translation_en_to_de')
    text_trans = translators(text)
    return text_trans[0]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate',methods=["POST"])
def translatetext():
    if request.method == "POST":
        data = request.form.to_dict()
        files = request.files['filename']
        filename = request.files['filename'].filename
        
        if len(data) >0:
            key,text = list(data.items())[0]

        if files:
            text = speech_to_text(files) 

        translated_text = translate(text)

        return render_template("index.html", response1 = text,response2=translated_text['translation_text'])
        
if __name__== "__main__":
    app.debug = True
    app.run()