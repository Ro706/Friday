import  pyttsx3 #this is a pyttsx3 library : pip install pyttsx3 : this library is used to convert text to speech
import datetime #this is a datetime library : pip install datetime : this library is used to get date and time
engine = pyttsx3.init() #here we are initializing pyttsx3
# engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.setProperty('voice', engine.getProperty('voices')[1].id) #here we are setting voice as female
    # Function to speak text
    engine.say(text) #this is a function to convert text to speech
    engine.runAndWait() #this is a function to run and wait
    
def wishme():
    hour = int(datetime.datetime.now().hour) #this is a datetime library : pip install datetime : this library is used to get date and time
    if hour>=0 and hour<12: 
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday. Please tell me how may I help you")
