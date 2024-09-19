from pipes import quote
import sqlite3
import os
import cv2
import subprocess
from playsound import playsound
import eel
import pyautogui
from engine.command import speak
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

def showvideo():
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture('www/assets/video/cyberbot.mp4')

# Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")

# Read until video is completed
    while(cap.isOpened()):
    
# Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
    # Display the resulting frame
            cv2.imshow('Isimm CyberBot V3.0', frame)
            cv2.setWindowProperty('Isimm CyberBot V3.0', cv2.WND_PROP_TOPMOST, 1)
        
    # Press Q on keyboard to exit
            if cv2.waitKey(20) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyWindow('Isimm CyberBot V3.0')
                break

# Break the loop
        else:
            break
    cap.release() 
    cv2.destroyWindow('Isimm CyberBot V3.0')  

# When everything done, release
# the video capture object
    
def showimages():
    img1=cv2.imread('www/assets/img/1.jpg')
    img2=cv2.imread('www/assets/img/2.jpg')
    img3=cv2.imread('www/assets/img/3.jpg')
    img4=cv2.imread('www/assets/img/4.jpg')
    img5=cv2.imread('www/assets/img/5.jpg')
    img6=cv2.imread('www/assets/img/6.jpg')
    img7=cv2.imread('www/assets/img/7.jpg')
    img8=cv2.imread('www/assets/img/8.jpg')
    img9=cv2.imread('www/assets/img/9.jpg')
    img10=cv2.imread('www/assets/img/10.jpg')
    img11=cv2.imread('www/assets/img/11.jpg')
    img12=cv2.imread('www/assets/img/12.jpg')
    img13=cv2.imread('www/assets/img/13.jpg')
    img14=cv2.imread('www/assets/img/14.jpg')
    (h, w) = img1.shape[:2]
    new_width2 = 500
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
    resized_image12= cv2.resize(img12, (500, 400))
    resized_image13= cv2.resize(img13, (new_width2, new_height2))
    resized_image14= cv2.resize(img14, (new_width2, new_height2))
    speak("CPU is a Robotics Club at ISIMM Created in 2018, it focuses on enhancing students' skills in robotics and development. Through hands-on activities, members gain valuable experience in teamwork and collaboration, while also building new friendships. The club regularly organizes competitions,it also providing students with opportunities to showcase their talents and put their skills to the test throught projects")
    speak("The journey start with the integration day which will be followed with building team day ")
    cv2.imshow('integration day',resized_image5)
    cv2.setWindowProperty("integration day", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('Team building day',resized_image6)
    cv2.setWindowProperty('Team building day', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('Team building day2',resized_image1)
    cv2.setWindowProperty('Team building day2', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('Team building day2')
    cv2.destroyWindow('Team building day')
    cv2.destroyWindow('integration day')
    speak("I will add that the CPU activitis contains worckshops in the developpment and robotic domains  ")
    cv2.imshow('soft step day',resized_image2)
    cv2.setWindowProperty('soft step day', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('worckshop day',resized_image4)
    cv2.setWindowProperty('worckshop day', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('worckshop1',resized_image7)
    cv2.setWindowProperty('worckshop1', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    speak("so far it is a chaine of training sessions and worckshops to develop the student skill ")
    cv2.imshow('worckshop2',resized_image8)
    cv2.setWindowProperty('worckshop2', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('worckshop3',resized_image9)
    cv2.setWindowProperty('worckshop3', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    speak("i will say that we have a professional stuff for this kind of jobs ,they have the talent to give an efficient performance and hight level knowledge ")
    cv2.imshow('worckshop4',resized_image10)
    cv2.setWindowProperty('worckshop4', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.imshow('worckshop5',resized_image11)
    cv2.setWindowProperty('worckshop5', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('worckshop5')
    cv2.destroyWindow('worckshop4')
    cv2.destroyWindow('worckshop3')
    cv2.destroyWindow('worckshop2')
    cv2.destroyWindow('worckshop1')
    cv2.destroyWindow('worckshop day')
    cv2.destroyWindow('soft step day')
    cv2.imshow('cpu',resized_image12)
    cv2.setWindowProperty('cpu', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    speak("as we see here our dev team had participated at the TCPC Competitiont , it's an honor to see young talented students grwing up and moving forward")
    cv2.imshow('big pics',resized_image13)
    cv2.setWindowProperty('big pics', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    speak("however i will never forget the robotic competitions which is a place for competetive minds ")
    cv2.imshow('festival',resized_image14)
    cv2.setWindowProperty('festival', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('festival')
    cv2.destroyWindow('big pics')
    cv2.destroyWindow('cpu')
    
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
                        speak("can t open")
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
        porcupine=pvporcupine.create(keywords=["americano","computer"]) 
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
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name

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
    speak("It's my pleasure to "+ query)
    query = query + "in three lines"
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine/cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

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