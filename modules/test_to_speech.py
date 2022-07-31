'''
Module to convert text to speech
'''
import pyttsx3

class Talker:  #Clase Talker, todo el uso del engine Texto to Speech
    '''
    Class to speack text
    '''
    def __init__(self):
        self.__engine = pyttsx3.init() # Inicializo el motor para empezar a utilizarlo
        self.rate = 150   # Velocidad del habla
        self.voices = None   # Voces disponibles
        self.actual_voice = None   # Voce utilizada Actualmente.

        self.init_voices()
        self.set_rate_voice()

    def init_voices(self):
        '''
        Review if are voices installed and select the first
        '''
        self.voices = self.__engine.getProperty("voices")   # Me regresa todas las voces disponibles
        if len(self.voices) > 0:
            self.actual_voice = self.voices[0].name
            print("Se inicializan las voces")

    def set_rate_voice(self):
        '''
        the talker speed
        '''
        self.__engine.setProperty("rate", self.rate)

    def talk(self, text:str):
        '''
        Machine talk method
        * text: the text to say
        '''
        self.__engine.say(text)   # Dice lo que le pasemos como parametro
        self.__engine.runAndWait()
 
    def show_all_voices(self): # Muestra todas las voces.
        '''
        show all voices installed on OS
        '''
        for i,voice in enumerate(self.voices):
            print(str(i) + ")  Voz: " + voice.name)

    def set_voice(self, voice:int): #Cambia la voz
        '''
        change the voice for the new one select
        * voice: the new voice

        For know all the voices installed use ``show_all_voice``
        '''
        self.actual_voice = self.voices[voice].name
        self.__engine.setProperty("voice", self.voices[voice].id)

