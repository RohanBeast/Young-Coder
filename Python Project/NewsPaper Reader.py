import requests
import json
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    a = engine.getProperty("rate")
    engine.setProperty("rate", 120)
    engine.say(audio)
    engine.runAndWait()


def newsGet():
    a = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=83d00214bbee4a51b4221c8c4481c918")
    b = json.loads(a.text)
    c = b["articles"]
    i = 0

    for item in range(len(c)):
        d = c[i]
        print(d["title"])
        speak(d["title"])

        i += 1
    
newsGet()
