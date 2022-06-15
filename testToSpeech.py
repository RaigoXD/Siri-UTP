import pyttsx3

class Talker:  #Clase Talker, todo el uso del engine Texto to Speech
    def __init__(self):
        self.__engine = pyttsx3.init() # Inicializo el motor para empezar a utilizarlo
        self.rate = 150; # Velocidad del habla
        self.voices = None; # Voces disponibles
        self.actualVoice = None; # Voce utilizada Actualmente.
        
        self.initVoices();
        self.setRateVoice(); 
        
    def initVoices(self):
        self.voices = self.__engine.getProperty("voices"); # Me regresa todas las voces disponibles
        if len(self.voices) > 0:
            self.actualVoice = self.voices[1].name;
            print("Se inicializan las voces");

    def setRateVoice(self):
        self.__engine.setProperty("rate", self.rate);
        
    def talk(self, text:str):
        self.__engine.say(text); # Dice lo que le pasemos como parametro
        self.__engine.runAndWait();
        
    def showAllVoices(self): # Muestra todas las voces.
        for i,voice in enumerate(self.voices):  
            print(str(i) + ")  Voz: " + voice.name);

    def setVoice(self, voice:int): #Cambia la voz
        self.actualVoice = self.voices[voice].name;
        self.__engine.setProperty("voice", self.voices[voice].id);
