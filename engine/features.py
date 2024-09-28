from pipes import quote
import sqlite3
import os
import cv2
import subprocess
from playsound import playsound
import eel
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.config import *
from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat
import pywhatkit as kit
import webbrowser
import pvporcupine
import pyaudio
import struct
import time


con = sqlite3.connect("Alpha.db")
cursor = con.cursor()

# playing assistant sound function 
@eel.expose
def playAssistantSound():

    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)

#################################
def showimages():
    img1=cv2.imread('www/assets/img/img6.jpg')
    img2=cv2.imread('www/assets/img/2.jpg')
    img3=cv2.imread('www/assets/img/3.jpg')
    img4=cv2.imread('www/assets/img/4.jpg')
    img5=cv2.imread('www/assets/img/5.jpg')
    img6=cv2.imread('www/assets/img/6.jpg')
    img7=cv2.imread('www/assets/img/7.jpg')
    img8=cv2.imread('www/assets/img/8.jpg')
    img9=cv2.imread('www/assets/img/9.jpg')
    img10=cv2.imread('www/assets/img/integ2.jpg')
    img11=cv2.imread('www/assets/img/11.jpg')
    img12=cv2.imread('www/assets/img/img14.jpg')
    img13=cv2.imread('www/assets/img/12.jpg')
    img14=cv2.imread('www/assets/img/14.jpg')
    (h, w) = img1.shape[:2]
    new_width2 = 700
    aspect_ratio = h / w
    new_height2 = int(new_width2 * aspect_ratio)

# Resize the image
    resized_image1 = cv2.resize(img1, (new_width2, new_height2))
    resized_image2 = cv2.resize(img2, (new_width2, new_height2))
    resized_image3 = cv2.resize(img3, (new_width2, new_height2))
    resized_image4 = cv2.resize(img4, (new_width2, new_height2))
    resized_image5 = cv2.resize(img5, (new_width2, new_height2))
    resized_image6 = cv2.resize(img6, (400, 500))
    resized_image7 = cv2.resize(img7, (new_width2, new_height2))
    resized_image8 = cv2.resize(img8, (new_width2, new_height2))
    resized_image9 = cv2.resize(img9, (new_width2, new_height2))
    resized_image10 = cv2.resize(img10, (new_width2, new_height2))
    resized_image11 = cv2.resize(img11, (new_width2, new_height2))
    resized_image12= cv2.resize(img12, (400, 500))
    resized_image13= cv2.resize(img13, (new_width2, new_height2))
    resized_image14= cv2.resize(img14, (new_width2, new_height2))

    speak("CPU Club at ISIMM was established in 2018 with a clear mission: to enhance students skills in development, problem-solving, and robotics. Through regular competitions and engaging projects, the club provides students with valuable opportunities to showcase their talents and put their skills to the test")
    
    speak("You can see various innovative projects created by Club CPU seniors during Integration Day")
    cv2.imshow('integration day',resized_image5)
    cv2.setWindowProperty("integration day", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('integration day')

    cv2.imshow('Team building day2',resized_image1)
    cv2.setWindowProperty('Team building day2', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('Team building day2')
    
    speak("They have a professional and talented staff working on improving the level of student knowledge in development through programming languages")

    cv2.imshow('Workshop1',resized_image7)
    cv2.setWindowProperty('Workshop1', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('Workshop1')


    cv2.imshow('workshop2',resized_image8)
    cv2.setWindowProperty('workshop2', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('workshop2')

    cv2.imshow('Workshop3',resized_image9)
    cv2.setWindowProperty('Workshop3', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('Workshop3')

    speak("These coding rockstars aren't just crushing it at TCPC and mind-bending problem-solving showdowns - they're cooking up epic workshops to turn fellow students into puzzle-busting prodigies!")
    cv2.imshow('big pics',resized_image13)
    cv2.setWindowProperty('big pics', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('big pics')

    
    speak("Not just coding wizards, these CPU Club seniors are also robotics gurus, transforming newbies into tech maestros through hands-on, mind-blowing projects!")
    cv2.imshow('Workshop4',resized_image10)
    cv2.setWindowProperty('Workshop4', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('Workshop4')

    cv2.imshow('Workshop5',resized_image11)
    cv2.setWindowProperty('Workshop5', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('Workshop5')

    cv2.imshow('cpu',resized_image12)
    cv2.setWindowProperty('cpu', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=2000)
    cv2.destroyWindow('cpu')

##############################################
    
def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")    
    query=query.replace("open","")  
    query.lower()  

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                  'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("can't open")
        except:
            speak("some thing went wrong")


def playYoutube(query):
        search_term = extract_yt_term(query)
        try:
            speak("playing "+search_term+" on youtube")
            kit.playonyt(search_term)
        except:
            speak("not found on youtube")    
                    


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=[ASSISTANT_NAME,"americano","computer"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

                
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+216'):
            mobile_number_str = '+216' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "starting video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)


# chat bot 
def chatBot(query):

    query = query + "in three lines without saying in three lines "
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
    
    # HugChat is an unofficial Python client for HuggingFace's chat API.
    # HugChat: This is a Python library that allows you to interact with HuggingFace's
    # conversational AI models through their chat interface

# android automation

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(229, 1411)
    time.sleep(5)
    #start chat
    tapEvents(474, 1433)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(307, 348)
    # tap on input
    tapEvents(350, 1478)
    #message
    adbInput(message)
    #send
    tapEvents(644, 996)
    speak("message send successfully to "+name)







      