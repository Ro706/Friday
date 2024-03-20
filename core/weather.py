# this file is create to tell weather in city nagpur
#and this will help user to know weather in nagpur
import requests #this is a requests library : pip install requests : this library is used to send http requests
import pyttsx3 # this is a pyttsx3 library : pip install pyttsx3 : this library is used to convert text to speech
import json # this is a json library : this library is used to convert json to python

#main code
engine = pyttsx3.init() #here we are initializing pyttsx3
# engine.setProperty('voice', engine.getProperty('voices')[1].id) #here we are setting voice as female
def speak(text): #this is a function to convert text to speech
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Function to speak text
    engine.say(text)
    engine.runAndWait()

#form here we are creating a class weather to get weather of nagpur city
class weather:
    def __init__(self,city) :  #here we declare a constructor in python which takes city as an argument
        self.city = city #here we are assigning city to self.city
    def weather(self):
        api_key ='04018081b69cca6f721c5ed1a46be071' #this is a api key from openweathermap.org
        base_url = 'https://api.openweathermap.org/data/2.5/weather?' # this is a base url from openweathermap.org
        url = base_url+'appid='+api_key+'&q='+self.city+'&units=metric' #this is a url from openweathermap.org ( we are adding api_key and city to url )
        response = requests.get(url) # here we are sending http request to url
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
        
def tellmeTodaysWeather(): #this function will tell weather of nagpur city
    obj = weather("Nagpur")
    obj.weather()

if __name__=="__main__":
    tellmeTodaysWeather()

