

import speech_recognition as sr
import pyaudio as audio
import pprint as pp
from testToSpeech import *

talker = Talker();

talker.setVoice(voice=3);

talker.talk(text="Mi casa es de color verde");

talker.showAllVoices();

# receptor = sr.Recognizer(); # Este objeto tiene todo lo importante con el reconocimiento
# receptor.dynamic_energy_threshold = True; # Para noise dinamico
# receptor.pause_threshold = 0.5; # Tiempo en segundos que dura en terminar un audio.

# try:
#     with sr.Microphone() as source: # 6
#         receptor.adjust_for_ambient_noise(source, duration=1);
#         #pp.pprint(source.get_pyaudio())
#         print(receptor.energy_threshold);
#         print("Escuchando...");
#         voice = receptor.listen(source);
#         rec = receptor.recognize_google(voice,language="es-CO");
#         print(rec);
# except:
#     pass
