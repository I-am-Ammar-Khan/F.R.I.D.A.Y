import pyttsx3
import pyjokes
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser
import os
import PyPDF2
from playsound import playsound
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def Suggestions():
    qstq = ["Try saying for open YouTube", "Try saying for 'Read Think and grow Rich",
            "Try saying for 'what's the Time", "Try saying for 'wish me Friday",
            "Try saying for 'open command prompt", "Try saying for 'open notepad", "Try saying for 'play beliver",
            "Try saying for 'who is leonardo da vinci", "Try saying for 'who is Elon Musk", "Try saying for 'who is necola Tesla"]
    suggestion = random.choice(qstq)
    print(suggestion)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        playsound('E:\PYTHON\Real-life-Problem\F.R.I.D.A.Y\when.mp3')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return command


def wishme():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    if hour <= 12:
        speak('Good Morning boss')
    elif hour > 12 and hour < 18:
        speak('Good Afternoon boss')

    else:
        speak('Good Evening boss')


def pdfreads():
    book = open('ThinkAndGrowRich.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print(pages)
    speak('boss where should i start reading ')
    pno = int(input("Enter the page number : "))
    page = pdfreader.getPage(pno)
    text = page.extractText()
    speak(text)


if __name__ == "__main__":
    wishme()
    while True:
        command = take_command().lower()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            speak('Playing ' + song)
            pywhatkit.playonyt(song)
        elif'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('it is currently '+time)
        elif 'who is' in command:
            speak("searching in wikipedia")
            person = command.replace('who is', '')
            speak('According to wikipedia')
            info = wikipedia.summary(person, 2)
            print(info)
            speak(info)
        elif 'who are you' in command:
            speak('I am your voice assistance Friday')

        elif'who invent' in command:
            speak('the great you')

        elif 'will you marry me' in command:
            speak('sorry I am with relationship with google')

        elif 'i am very angry right now' in command:
            speak('but why boss')

        elif 'i like you' in command:
            speak('I like you too')

        elif 'i miss you' in command:
            speak('I miss you too')

        elif ' i need some advice' in command:
            speak('about what boss')

        elif 'you were wrong' in command:
            speak('i am sorry')

        elif 'open chrome' in command:
            webbrowser.open('https://www.google.com/')
            speak('opening google chrome')

        elif 'close chrome' in command:
            os.system('taskkill /f /im chrome.exe')

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")

        elif 'open how to' in command:
            webbrowser.open("https://www.wikihow.com/Main-Page")
            speak("opening wikihow")

        elif 'open 10fastfinger' in command:
            webbrowser.open('https://10fastfingers.com/typing-test/english')

        elif 'open code' in command:
            # codePath = "E:\\VS Code\Microsoft VS Code\\Code.exe"
            codePath = "C:\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'close code' in command:
            os.system('taskkill /f /im Code.exe')

        elif 'open notepad' in command:
            speak('opening notepad')
            nppath = "C:\Windows\System32\\notepad.exe"

            os.startfile(nppath)
        elif 'close notepad' in command:
            os.system('taskkill /f /im notepad.exe')

        elif 'think and grow rich' in command:
            pdfreads()

        elif 'my website' in command:
            speak('opening your website')
            webbrowser.open('https://code-ammar.blogspot.com/')

        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'open command prompt' in command:
            os.system("start cmd")

        elif 'wish me' in command:
            wishme()

        elif 'you can sleep ' in command:
            speak('ok  I am going to sleep you can call me anytime')
            break

    while True:
        hotword = take_command()
        if 'wake up ' in hotword:
            speak('I am always here for you boss')
            take_command()
        elif 'bye bye' in hotword:
            speak('Thanks for using me Have a gooday boss')
            os.system().exit()
