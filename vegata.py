import pyttsx3
import speech_recognition
import requests
import time
engine = pyttsx3.init()
myip =  "http://192.168.0.105"

voice = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        print("i am listening...")
        audio = voice.listen(mic)
    try:
        input_text = voice.recognize_google(audio)
    except:
        input_text = ""                        
    if input_text == "":                               
            input_text = "i don't hear about"
            engine.say(input_text)
    elif input_text == "turn on light 1":
            requests.get (myip + "/2/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn on light one":
            requests.get (myip + "/2/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light one":
            requests.get (myip + "/2/off")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light 1":
            requests.get (myip + "/2/off")
            print(input_text)
    elif input_text == "turn on light two":
            requests.get (myip + "/4/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn on light 2":
            requests.get (myip + "/4/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light two":
            requests.get (myip + "/4/off")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light 2":
            requests.get (myip + "/4/off")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn on light three":
            requests.get (myip + "/5/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn on light 3":
            requests.get (myip + "/5/on")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light three":
            requests.get (myip + "/5/off")
            print(input_text)
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light 3":
            requests.get (myip + "/5/off")
            print("turn off all light")
            engine.say(" ok....." + input_text)
    elif input_text == "turn off light":
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
    elif input_text == "turn on light":
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
    elif input_text == "today":
        result = time.strftime("%d %B, %Y")
        engine.say(result)
    elif input_text == "hello":
        engine.say("what can i help you?")
    elif input_text == "thank you":
        engine.say("Have a great day!")
        engine.runAndWait()
        break
    elif input_text == "goodnight":
        engine.say("Good night, see you")
        engine.runAndWait()
        break
    elif input_text == "morning":
        engine.say("Have a great day!")
    elif input_text == "thanks":
        engine.say("Have a great day!")
        engine.runAndWait()
        break
    elif input_text == "love you":
        engine.say("thank you, love you too")
    elif input_text =="what time":
        result = time.strftime("%H ,%M")
        engine.say(result)
    elif input_text =="what's your name":
        engine.say("Vegata")
    elif input_text == "bye":
            engine.say("bye Sir")
            engine.runAndWait()
            break
    elif input_text == "bye-bye":
            engine.say("bye Sir")
            engine.runAndWait()
            break
    elif input_text == "quit":
            engine.say("bye Sir")
            engine.runAndWait()
            break
    engine.runAndWait()
            
