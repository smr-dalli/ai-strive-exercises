from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path
import requests
from transformers import pipeline
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import numpy as np
import os
import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone(device_index=2)
with mic as source:
    audio = r.listen(source)
audio_text = r.recognize_google(audio)
print(audio_text)
print(type(audio_text))


