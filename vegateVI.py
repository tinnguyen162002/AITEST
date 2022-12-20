import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio
import time
import playsound
import requests
myip = "http://192.168.0.105"
def speak(text):
    tts = gTTS(text=text,lang='vi')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
r = sr.Recognizer()
with sr.Microphone() as source:
 print("Mời bạn nói: ")
 audio = r.listen(source)
try:
 text = r.recognize_google(audio,language="vi-VI")
 print("Bạn -->: {}".format(text))
except:
  if input_text == "":                        
             print(input_text)
if input_text == "bật đèn 1":
            requests.get (myip + "/2/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "bật đèn một":
            requests.get (myip + "/2/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt đèn một":
            requests.get (myip + "/2/off")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt đèn 1":
            requests.get (myip + "/2/off")
            print(input_text)
elif input_text == "bật đèn hai":
            requests.get (myip + "/4/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "bật đèn 2":
            requests.get (myip + "/4/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt đèn hai":
            requests.get (myip + "/4/off")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt đèn 2":
            requests.get (myip + "/4/off")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "bật đèn ba":
            requests.get (myip + "/5/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "bật đèn 3":
            requests.get (myip + "/5/on")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt đèn ba":
            requests.get (myip + "/5/off")
            print(input_text)
            engine.say(" ok....." + input_text)
elif input_text == "tắt hết đèn 3":
            requests.get (myip + "/5/off")
            print("turn off all light")
            engine.say(" ok....." + input_text)
elif input_text == "tắt hết đèn":
            requests.get (myip + "/5/off")
            requests.get (myip + "/4/off")
            requests.get (myip + "/2/off")
            print("turn off all light")
            engine.say(" ok....." + "turn off al light")
elif input_text == "off light":
            requests.get (myip + "/5/off")
            requests.get (myip + "/4/off")
            requests.get (myip + "/2/off")
            print(input_text)
            engine.say(" ok....." + "turn off all light")
elif input_text == "bật hết đèn":
            requests.get (myip + "/5/on")
            requests.get (myip + "/4/on")
            requests.get (myip + "/2/on")
            print("turn on all light")
            engine.say(" ok....." + "turn on all light")
elif input_text == "on light":
            requests.get (myip + "/5/on")
            requests.get (myip + "/4/on")
            requests.get (myip + "/2/on")
            print("turn on all light")
            engine.say(" ok....." + "turn on all light")            
engine.runAndWait()
