import requests
import pyttsx3 
import json

#main code
engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Function to speak text
    engine.say(text)
    engine.runAndWait()
class weather:
    def __init__(self,city) : 
        self.city = city
    def weather(self):
        api_key ='04018081b69cca6f721c5ed1a46be071'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        url = base_url+'appid='+api_key+'&q='+self.city+'&units=metric'
        response = requests.get(url)
        x=response.json()
        if x['cod']!=401:
            print ('city name:',x['name'])
            print ('weather:',x['weather'][0]['main'])
            print ('temp:',x['main']['temp'],"degree celsius")
            print ('minimum temp:',x['main']['temp_min'],"degree celsius")
            print ('max temp:',x['main']['temp_max'],"degree celsius")
            speak("city name: "+x['name'])
            speak("weather: "+x['weather'][0]['main'])
            speak("temperature is : "+str(x['main']['temp'])+" degree celsius")
        else:
            print ('city not found')
        
def tellmeTodaysWeather():
    obj = weather("Nagpur")
    obj.weather()

if __name__=="__main__":
    tellmeTodaysWeather()

