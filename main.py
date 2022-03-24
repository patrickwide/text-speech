import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')
# getting details of current speaking rate

#getting details of current voice
voices = engine.getProperty('voices')
#changing index, changes voices. 1 for female
engine.setProperty('voice', voices[1].id)
engine.say("Hello World!")
engine.runAndWait()

#getting details of current voice
voices = engine.getProperty('voices')
#changing index, changes voices. 1 for female
engine.setProperty('voice', voices[0].id)
engine.say("Hello World!")
engine.runAndWait()








