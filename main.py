import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import webbrowser
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os
import pywhatkit
import datetime
import subprocess
import requests
from bs4 import BeautifulSoup
import speedtest
import pyautogui
import keyboard
from Features.custom_voice import speak
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
from pygame import mixer
mixer.init()
from plyer import notification
import psutil

root=Tk()
root.geometry("750x750")
def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("NaniGPT_Animation.gif")
    lbl=Label(root)
    lbl.place(x=0,y=0)
    i=0
    for img in ImageSequence.Iterator(img):
        img=img.resize((750,750))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.0078125)
    root.destroy()
play_gif()
root.mainloop()


recognizer=sr.Recognizer()
genai.configure(api_key="Your API KEY HERE")
model = genai.GenerativeModel("gemini-1.5-flash")
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

with sr.Microphone() as source:
    try:
        speak("May I know who am I talking to?")
        recognizer = sr.Recognizer()
        audio = recognizer.listen(source)
        transcription = recognizer.recognize_google(audio)
        name=transcription.lower()
    except Exception as ex:
        print(ex)
def wish():
    hou = int(datetime.datetime.now().hour)
    if hou>=0 and hou<=12:
        speak(f"Good morning {name}!")
    elif hou>=12 and hou<=18:
        speak(f"Good afternoon {name}!")
    else:
        speak(f"Hello {name}! Good evening!")
    speak("I'm Naani! I'm your personal AI Friend! Enter the abbreviated form of the language in which you want to communicate with me so that I can respond in your native tongue.")
    
wish()
langinput=input("Enter the short form of the language in which you want to speak:")

def takeCommand():
    while True:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() == "nani":
                speak(f"yes {name}! Tell me")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0)
                    print("Waiting for your message!")
                    audio = recognizer.listen(source, timeout=None)
                    print("Done Recording")
                    try:
                        print("Recognising!")                        
                        result = recognizer.recognize_google(audio, language=str(langinput))
                    except Exception as ex:
                        print(ex)
                lquery=GoogleTranslator(source=langinput, target='en').translate(str(result))
                print(f"Your command: {lquery}")
                return lquery
            elif transcription.lower() == "bye":
                break
            
        except Exception as ex:
            print(ex)

def Reply(question):
    prompt=f'Nani: {question}\n '
    answer = model.generate_content(question)
    print(answer.text)
    aquery=GoogleTranslator(source='en', target=langinput).translate(str(answer.text))
    print(f"My Answer: {aquery}")
    tts = gTTS(text=aquery, lang=langinput)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
    return aquery

def check_notifications():
    try:
        notifications = notification.get_notification()
        if notifications:
            print("Notifications:")
            for notify in notifications:
                print(f"Title: {notify.title}, Message: {notify.message}")
        else:
            print("No notifications found.")
    except Exception as e:
        print(f"Error checking notifications: {e}")

def close_app(app_name):
    try:
        os.system(f'TASKKILL /F /IM {app_name}.exe')
        print(f"{app_name} closed successfully.")
    except Exception as e:
        print(f"Error closing {app_name}: {e}")


def webapps():
    if "whatsapp web" in query:
        webbrowser.open("https://web.whatsapp.com")
    elif "instagram" in query:
        webbrowser.open("https://www.instagram.com")
    elif "gmail" in query:
        webbrowser.open("https://www.gmail.com")
    elif "netflix" in query:
        webbrowser.open("https://www.netflix.com")
    elif "zee5" in query:
        webbrowser.open("https://www.zee5.com")
    elif "amazon" in query:
        webbrowser.open("https://www.amazon.in")
    elif "prime" in query:
        webbrowser.open("https://www.primevideo.com")
    elif "hotstar" in query:
        webbrowser.open("https://www.hotstar.com")
    elif "photos" in query:
        webbrowser.open("https://photos.google.com")
    elif "google" in query:
        webbrowser.open("https://www.google.com")

def volumeup():
    if "increase volume" in query:
        pyautogui.press("volumeup")
def volumedown():
    if "decrease volume" in query:
        pyautogui.press("volumedown")
def volmute():
    if "mute" in query:
        pyautogui.press("volumemute")

def get_battery_info():
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        power_plugged = battery.power_plugged

        if power_plugged:
            status = "Charging"
        else:
            status = "Discharging"

        a=print(f"Battery Status: {status}")
        speak(status)
        b=print(f"Battery Percentage: {percent}%")
        speak(percent)
    except Exception as e:
        print(f"Error: {e}")

while True:
    query = takeCommand().lower()

    if 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('Current time is' + time)
    
    elif 'play' and 'youtube' in query:
        av=query.replace('play',"")
        speak("Playing"+av)
        pywhatkit.playonyt(av)    

    elif 'bluetooth' in query:
        speak(f"Yes {name}, on it")
        keyboard.press_and_release('windows+a')
        pyautogui.sleep(3)
        pyautogui.click(x=1645, y=593)
        pyautogui.sleep(3)
        pyautogui.press('esc')
    elif 'wifi' in query:
        speak(f"Yes {name}, on it")
        keyboard.press_and_release('windows+a')
        pyautogui.sleep(3)
        pyautogui.click(x=1512, y=593)
        pyautogui.sleep(3)
        pyautogui.press('esc')
    elif 'airplane' in query:
        speak(f"Yes {name}, on it")
        keyboard.press_and_release('windows+a')
        pyautogui.sleep(3)
        pyautogui.click(x=1825, y=578)
        pyautogui.sleep(3)
        pyautogui.press('esc')
    elif 'hotspot' in query:
        speak(f"Yes {name}, on it")
        keyboard.press_and_release('windows+a')
        pyautogui.sleep(3)
        pyautogui.press('down')
        pyautogui.click(x=1697, y=579)
        pyautogui.sleep(3)
        pyautogui.press('esc')
    elif 'battery saver' in query:
        speak(f"Yes {name}, on it")
        keyboard.press_and_release('windows+a')
        pyautogui.sleep(3)
        pyautogui.click(x=1678, y=697)
        pyautogui.sleep(3)
        pyautogui.press('esc')

    elif "open" in query:
        app_name=query.replace('open','')
        speak("opening"+app_name)
        pyautogui.press('super')
        pyautogui.sleep(1.0)
        pyautogui.typewrite(app_name)
        pyautogui.sleep(1.5)
        pyautogui.press('enter')

    elif "switch" in query:
        speak(f"ok {name}, switching app")
        pyautogui.hotkey('alt','tab')
    
    elif "open" and "instagram" in query:
        webapps()
    elif "open" and "gmail" in query:
        webapps()
    elif "open" and "netflix" in query:
        webapps()
    elif "open" and "amazon" in query:
        webapps()
    elif "open" and "prime" in query:
        webapps()
    elif "open" and "hotstar" in query:
        webapps()
    elif "open" and "photos" in query:
        webapps()
    elif "open" and "zee5" in query:
        webapps()
    elif "open" and "google" in query:
        webapps()
    
    elif "temperature" in query:
        search=query
        url=f"https://www.google.com/search?q={search}"
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
    elif "speed" in query:
        st = speedtest.Speedtest()
        dl=st.download()
        dls=dl/1000000
        up=st.upload()
        ups=up/1000000
        speak(f"Sir, we have {dls} mega bit per second download speed." f"and {ups} mega bit of upload speed right now!")
    elif "spotify" in query:
        with sr.Microphone() as source:
            try:
                speak("Tell me the song name")
                recognizer = sr.Recognizer()
                audio = recognizer.listen(source)
                transcription = recognizer.recognize_google(audio)
                speak(f"here you go {name}")
                song=transcription.replace('play',"")
                song=transcription.replace('spotify',"")
                song=transcription.replace('song',"")
                song=transcription.replace('songs',"")
                webbrowser.open(f'https://open.spotify.com/search/{song}')
                pyautogui.sleep(15)
                pyautogui.click(x=1031, y=348)
            except Exception as ex:
                print(ex)                     
    elif "location" in query:
        with sr.Microphone() as source:
            try:
                speak("Tell me the place name to locate")
                recognizer = sr.Recognizer()
                audio = recognizer.listen(source)
                location = recognizer.recognize_google(audio)
                url=f"https://www.google.com/maps/place/{location}"
                speak(f"Locating {str(location)}")
                webbrowser.open(url)
            except Exception as ex:
                print(ex)

    elif "increase volume" in query:
        volumeup()
    elif "decrease volume" in query:
        volumedown()
    elif "mute" in query:
        volmute()

    elif "shutdown" in query:
        speak(f"Sure {name}, shutting down your pc")
        keyboard.press_and_release('windows+d')
        pyautogui.sleep(1.5)
        pyautogui.hotkey('alt','f4')
        pyautogui.sleep(1.5)
        pyautogui.press('enter')
        '''pyautogui.press('super')
        pyautogui.sleep(2)
        pyautogui.click(x=1274, y=960)
        pyautogui.sleep(2)
        pyautogui.click(x=1285, y=867)'''
    elif "restart" in query:
        speak(f"Sure {name}, restarting your pc")
        keyboard.press_and_release('windows+d')
        pyautogui.sleep(1.5)
        pyautogui.hotkey('alt','f4')
        pyautogui.sleep(1.5)
        pyautogui.press('down')
        pyautogui.sleep(1.5)
        pyautogui.press('enter')
        '''pyautogui.press('super')
        pyautogui.sleep(2)
        pyautogui.click(x=1274, y=960)
        pyautogui.sleep(2)
        pyautogui.click(x=1285, y=921)'''
    elif "lock" in query:
        speak(f"Sure {name}, locking your pc")
        keyboard.press_and_release('windows+d')
        pyautogui.sleep(1.5)
        pyautogui.hotkey('alt','f4')
        pyautogui.sleep(1.5)
        pyautogui.press('up')
        pyautogui.sleep(1.5)
        pyautogui.press('enter')
    elif "notification" in query:
        check_notifications()
    elif "battery" in query:
        get_battery_info()
    
    elif "close" in query:
        try:
            app_name=query.replace('close','')
            lapp_name=app_name.lower()
            os.system(f'TASKKILL /F /IM {lapp_name}.exe')
            print(f"{lapp_name} closed successfully.")
        except Exception as e:
            print(f"Error closing {lapp_name}: {e}")
    
    elif 'bye' in query:
        break
    else:
        Reply(query)