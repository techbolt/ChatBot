import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import requests
import datetime
import os
import pyautogui
import keyboard
import random
import webbrowser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification
from pygame import mixer
import subprocess



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding....")
        query = r.recognize_google(audio,language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "take rest" in query:
                    speak("Ok sir, You can call me anytime.")
                    break

                elif "thank you" in query:
                    speak("You're welcome, sir")

                elif "play" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "launch" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "pause" in query:
                    pyautogui.press("k")
                elif "resume" in query:
                    pyautogui.press("k")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted, sir.")
                elif "volume up" in query or "increase the volume" in query:
                    from keyboard import volumeup
                    speak("turning volume up")
                    volumeup()
                elif "volume down" in query or "decrease the volume" in query:
                    from keyboard import volumedown
                    speak("turning volume down")
                    volumedown()
                elif "tired" in query:
                    speak("Playing your favourite playlist sir.")
                    webbrowser.open("https://music.amazon.in/my/playlists/8240b65a-605c-4287-ac36-0140f0544011")
                    sleep(3.0)
                    pyautogui.click(570,490)
                    sleep(1.0)
                    pyautogui.click(570,490)
                elif "shutdown" in query:
                    os.system("shutdown /s /t 1")
                elif "message" in query:
                    from whatmsg import wmsg
                    wmsg(query)
                    speak("message sent sir")
                    sleep(1.0)
                    pyautogui.hotkey("ctrl","w")
                elif "take a screenshot" in query:
                    pyautogui.screenshot("scrshot.png")
                    speak("done sir")

                #elif "unlock my computer" in query:
                    #speak("Unlocking your computer sir")
                    #from pcUnlock import unlock
                    #kunlock()

                elif "lock my computer" in query:
                    speak("Locking your computer sir.")
                    cmd='rundll32.exe user32.dll, LockWorkStation'
                    subprocess.call(cmd)
                    
                elif "schedule my day" in query:
                    tasks = [] #emptyList
                    speak("Do you want to remove old tasks")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        numberoftask = int(input("enter the number of tasks:"))
                        i = 0
                        for i in range(numberoftask):
                            tasks.append(input("Enter the tasks:"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        numberoftask = int(input("enter the number of tasks:"))
                        for i in range(numberoftask):
                            tasks.append(input("Enter the tasks:"))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notifi.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My Schedule",
                        message = content,
                        timeout = 15
                    )
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "temperature" in query:
                    search = "temperature in lucknow is"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "sleep" in query:
                    speak("goodbye, sir.")
                    exit()




   