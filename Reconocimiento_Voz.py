from testToSpeech import *
from speechToText import *

talker = Talker();
talker.setVoice(voice=3);

listener = Listener();

string = listener.listen(umbral=True);

print(string);
talker.talk(string);
