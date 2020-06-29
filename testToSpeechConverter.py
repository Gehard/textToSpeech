import pyttsx3

# initialization

engine = pyttsx3.init()

#testing

engine.say('hi')
engine.say('this is my first text to speech converter program')
engine.say('everything i type here will be spoken by the program')

engine.runAndWait()