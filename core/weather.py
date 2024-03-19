import requests
import pyttsx3 
from bs4 import BeautifulSoup

#main code
engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Function to speak text
    engine.say(text)
    engine.runAndWait()

def weather(place):
        url = f"https://www.google.com/search?q=weather in {place}"
        r = requests.get(url)
        s = BeautifulSoup(r.text,'html.parser')
        temperature = s.find('div',class_='BNeawe').text
        a = f'current temperature in {place}: {temperature}'
        print(a)
        speak(a)
        
if __name__=="__main__":
    obj = weather("Nagpur")
    speak(obj.weather())

