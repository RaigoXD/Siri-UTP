

import speech_recognition as sr
import pyaudio as audio

receptor = sr.Recognizer();



try:
    with sr.Microphone() as source:
        print("Escuchando");
        voice = receptor.listen(source);
        rec = receptor.recognize_google(voice);
        print(rec);
except:
    pass

