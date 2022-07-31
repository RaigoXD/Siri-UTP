'''
Module for pass from speech to text
'''
import speech_recognition as sr

class Listener:
    '''
    Class for Hear and convert to text
    '''
    def __init__(self):
        self.receptor = sr.Recognizer()  #Instancio un objeto de la clase Recognizer
        self.receptor.dynamic_energy_threshold = True  # Para noise dinamico
        self.receptor.pause_threshold = 0.5  # Tiempo en segundos que dura en terminar un audio.

    def ambient_noise(self, time:int = 0.5): # time = Tiempo de duracion del analisis.
        '''
        Adjust the audio calculating the ambient noise
        * time: time in seconds for khow the ambien noise
        '''
        try:
            with sr.Microphone() as source:
                self.receptor.adjust_for_ambient_noise(source, duration=time)   # Creo un "umbral" de ruido, donde se habla y donde no.  
        except (AttributeError, sr.RequestError, sr.UnknownValueError, sr.WaitTimeoutError):
            print("Algo salio mal con el microfono.")

    def listen(self, umbral:bool = False):
        '''
        Listen and convert the speech to text
        * umbral: show or not the umbral
        '''
        self.ambient_noise()
        if umbral:
            print("El umbral es: " + str(self.get_umbral_noise()))
        try:
            with sr.Microphone() as source:
                print("Escuchando....")
                voice = self.receptor.listen(source)
                text = self.receptor.recognize_google(voice, language="es-CO")
                return text
        except (AttributeError, sr.RequestError, sr.UnknownValueError, sr.WaitTimeoutError):
            print("Algo salio mal en el Reconocimiento.")

        return "Existe algun problema con el microfono"

    def listen_from_audio(self, audio : str, umbral:bool = False) -> str:
        '''
        Listn from audio and convert the speech to text
        * audio: audio's path to use
        * umbral: show or not the umbral
        '''
        if umbral:
            print("El umbral es: " + str(self.get_umbral_noise()))
        try:
            with sr.AudioFile(audio) as source:
                print("Escuchando....")
                voice = self.receptor.record(source)
                text = self.receptor.recognize_google(voice, language="es-CO")
                return text
        except (AttributeError, sr.RequestError, sr.UnknownValueError, sr.WaitTimeoutError):
            print("Algo salio mal en el Reconocimiento.")

        return "Existe algun problema con el audio"


    def get_umbral_noise(self):  # retorno el "umbral"
        '''
        Return the umbral noise actual
        '''
        return self.receptor.energy_threshold
