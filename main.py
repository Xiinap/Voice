'''
pip install pyttsx3
'''
import pyttsx3

while True:
    #input
    word = input('Enter your text: ')

    engine = pyttsx3.init() 
    
    #settings
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    #saying
    engine.say(word)

#ending
engine.runAndWait()
