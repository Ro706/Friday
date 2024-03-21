import requests
import pyttsx3
import json
import datetime

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
class news:
    def __init__(self):
        self.url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a8c42b827a044f0b90d1d1fb314ef182"
    def news(self):
        news=requests.get(self.url).json()
        article=news["articles"]
        news_article=[]
        for arti in article:
            news_article.append(arti["title"])
        for i in range(len(news_article)):
            a=i+1,news_article[i]
            print (i+1,news_article[i])
            speak(news_article[i])
            
def news_report():
    obj = news()
    obj.news()
    
if __name__=="__main__":
    news_report()