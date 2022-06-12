

import speech_recognition as sr
import pyaudio as audio
import pprint as pp

receptor = sr.Recognizer();
receptor.dynamic_energy_threshold = True;
receptor.pause_threshold = 0.5;


try:
    with sr.Microphone() as source: # 6
        receptor.adjust_for_ambient_noise(source, duration=1);
        #pp.pprint(source.get_pyaudio())
        print(receptor.energy_threshold);
        print("Escuchando...");
        voice = receptor.listen(source);
        rec = receptor.recognize_google(voice,language="es-CO");
        print(rec);
except:
    pass

