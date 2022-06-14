import pyttsx3

class Talker:  #Clase Talker, todo el uso del engine Texto to Speech
    def __init__(self):
        self.__engine = pyttsx3.init()
        self.rate = 150;
        self.voices = None;
        self.actualVoice = None;
        
        self.initVoices();
        self.setRateVoice();
        
    def initVoices(self):
        self.voices = self.__engine.getProperty("voices");
        if len(self.voices) > 0:
            self.actualVoice = self.voices[1].name;
            print("Se inicializan las voces");

    def setRateVoice(self):
        self.__engine.setProperty("rate", self.rate);
        
    def talk(self, text:str):
        self.__engine.say(text);
        self.__engine.runAndWait();
        
    def showAllVoices(self):
        for i,voice in enumerate(self.voices):
            print(str(i) + ")  Voz: " + voice.name);

    def setVoice(self, voice:int):
        self.actualVoice = self.voices[voice].name;
        self.__engine.setProperty("voice", self.voices[voice].id);
