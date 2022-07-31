'''
main funtion for test the modules
'''
from os import path
from modules.test_to_speech import Talker
from modules.speech_to_text import Listener



AUDIOS_FILES = path.join(path.dirname(path.realpath(__file__)), "audios_pruebas")


if __name__ == '__main__':
    talker = Talker()
    talker.set_voice(voice=3)

    listener = Listener()
    print(AUDIOS_FILES)
    #listener.ambient_noise()
    Audio = path.join(AUDIOS_FILES, "Grabacion3.wav")

    string = listener.listen_from_audio(Audio,umbral=True)

    print(string)
    talker.talk(string)
