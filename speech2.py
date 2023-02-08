
import pyttsx3

while True:

    name=input("What is your name? ")
    engine = pyttsx3.init()
    engine.say(name)
    engine.runAndWait()
    