import pyttsx3
import time
import wikipedia
import os
import random
import webbrowser
import speech_recognition as sr

class Desktop:
    def __init__(self):
        pass

    def mic(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 800
            r.pause_threshold = 0.8
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print(f"User: {query}")
        except Exception as error:
            print(error)
        
        return query
    
    def speak(self, audio):
        print(f"Desktop: {audio}\n")
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

class Human_Interface(Desktop):
    def __init__(self):
        pass

    def greet(self):
        times = time.asctime(time.localtime()).split()
        ctime = times[3]

        ls = []

        for item in enumerate(ctime):
            if item[0] == 2:
                break
            else:
                ls.append(item[1])

        hour = int("".join(ls))
        
        if hour > 0 and hour < 12:
            self.speak("Good Morning Rohan")
        elif hour > 12 and hour < 16:
            self.speak("Good After Noon Rohan")
        else:
            self.speak("Good Evening Rohan")
    
    def main(self):
        while True:
            query = self.mic().lower()
            if "hello" in query or "hi" in query:
                self.speak("Hello Sir")

            elif "search for" in query or "look for" in query:
                try:
                    query = query.replace("search for ", "")
                except Exception:
                    query = query.replace("look for ")

                finally:
                    self.speak(f"Searching for {query}")
                    result = wikipedia.summary(query, sentences=3)
                    self.speak(f"According to wikipedia, the results are {result}")
            
            elif "what's the time" in query or "what is the time" in query:
                ctime = time.asctime(time.localtime()).split()[3]
                self.speak(ctime)
            
            elif "open google" in query:
                self.speak("Opening google, have a nice search")
                webbrowser.open("https://www.google.com")
            
            elif "open youtube" in query:
                self.speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com")
            
            elif "who are you" in query or "what is your name" in query:
                self.speak("Sir, I am Jarvis, a bot made by Rohan Tyagi. I can perform several actions by commands.")
            
            elif "play music" in query:
                self.speak("Playing Music, enjoy")

                os.chdir("C:/Users/admin/Music")
                mlist = os.listdir()
                mlist.remove("desktop.ini")
                mlist.remove("desktop (New).ini")

                rand = random.choices(mlist)[0]
                os.startfile(rand)
            

a = Human_Interface()
a.greet()
a.main()