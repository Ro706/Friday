import  pyttsx3 
import datetime
engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Function to speak text
    engine.say(text)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Friday. Please tell me how may I help you")
