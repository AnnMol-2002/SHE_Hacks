from urllib import request
import pyttsx3
import datetime
import pywhatkit

import requests
from bs4 import BeautifulSoup
 
import speech_recognition as s
w=pyttsx3.init()
def speak(a):
    w.say(a)
    w.runAndWait()

def recognise():
    l=s.Recognizer()
    with s.Microphone() as m:
        print("listening")
        voice=l.listen(m)
        try:
            command=l.recognize_google(voice)
            return command
        except:
            a="please say again"
            speak(a)
command = recognise()
print(command)
command=command.lower()

if 'chrome' in command:
    a="Opening Chrome...."
    speak(a)
    pywhatkit.search(command)

if 'time' in command:
    time=datetime.datetime.now().strftime("%I:%M:%p")
    print(time)
    speak(time)
h=['play','video','show']
if any(x in command for x in h ):
    b='Opening youtube....'
    speak(b)
    pywhatkit.playonyt(command)
    
k=['weather','temperature','climate']
if any(x in command for x in k):
    s="temperature in thrissur"
    url=f"https://www.google.com/search?q={s}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    speak(f"current{s} is {temp}")       
    print(f"current{s} is {temp}")
