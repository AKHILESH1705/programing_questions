import sys
import winspeech


winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

def speech_recognizer(result,listner):
    print("you said : %s" % result)
    if result == "stop":
        winspeech.stop_listening()
        sys.exit(0)
listner = winspeech.listen_for_anything(speech_recognizer)

while winspeech.is_listening():
    continue
    
