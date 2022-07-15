import speech_recognition as sr 
import pyaudio as audio  # Es necesario tener Pyaudio instalado en el sistema.


class Listener:
    
    def __init__(self):
        self.receptor = sr.Recognizer(); #Instancio un objeto de la clase Recognizer
        self.receptor.dynamic_energy_threshold = True; # Para noise dinamico
        self.receptor.pause_threshold = 0.5; # Tiempo en segundos que dura en terminar un audio.

    def ambientNoise(self, time:int = 1): # time = Tiempo de duracion del analisis.
        try:
            with sr.Microphone() as source:
                self.receptor.adjust_for_ambient_noise(source, duration=time);  # Creo un "umbral" de ruido, donde se habla y donde no.  
        except:
            print("Algo salio mal con el microfono.");
            
    def listen(self, umbral:bool = False):
        self.ambientNoise();
        if umbral:
            print("El umbral es: " + str(self.getUmbralNoise()));
            
        try:
            with sr.Microphone() as source:
                print("Escuchando....")
                voice = self.receptor.listen(source);
                text = self.receptor.recognize_google(voice, language="es-CO");
                return text;
        except:
            print("Algo salio mal en el Reconocimiento.");
        
        return "None";
    
    def getUmbralNoise(self):  # retorno el "umbral"
        return self.receptor.energy_threshold;
    