import pyttsx3 #pick the voice 
import speech_recognition as sr
import eel
import time
import threading
from engine.funct import showvideo


speak_thread = None

@eel.expose
def speak(text):
    global engine
    global speak_thread
    text = str(text)
    engine = pyttsx3.init()   
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Changing index, changes voices. 1 for female, 2 for male
    engine.setProperty('rate', 174)  # Setting up new voice speed (174 words per minute)    
    eel.DisplayMessage(text)
    eel.DisplayMessage(text)
    engine.say(text)
    # Start the speech in a separate thread
    # speak_thread = threading.Thread(target=engine.say, args=(text))
    # speak_thread.start()
    eel.recieverText(text)
    engine.runAndWait()

# @eel.expose
# def stop_speaking():
#     if speak_thread:
#         speak_thread.terminate()
#         print("Speech stopped")
#     else:
#         print("Not currently speaking")

@eel.expose
def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source :
    print('listening.....')
    eel.DisplayMessage('listening.....')
    eel.DisplayMessage('listening.....')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source, 10,6)

  try:
    print('Recognizing')
    eel.DisplayMessage('Recognizing.....')
    query = r.recognize_google(audio_data=audio,language='en-GB')
    eel.DisplayMessage('Recognizing.....')
    query = r.recognize_google(audio_data=audio,language='en-GB')
    print(f"user said :{query}")
    eel.DisplayMessage(query)
    time.sleep(2)
   
    eel.DisplayMessage(query)
    time.sleep(2)
   
  except Exception as e:
    return ""
  
  return query.lower()

@eel.expose
def allCommands(message=1):
  if message==1:
    query=takeCommand()
    print(query)
    eel.senderText(query)
  else:
     query=message
     eel.senderText(query)
  
  Q1=['join','which','recommend', 'best club']
  Q2=['about you','introduce yourself','is your name','your creators','created you']
  Q3=['committee' , 'comity']
  try:

    if "don't" in query in query:
      speak("I apologize, how can I help you?")

    elif "cpu club" in query:
      from engine.features import showimages
      showimages()

    elif any(word in query for word in Q1 ):
      speak("All clubs can provide you with additional information to enhance your knowledge, but Club CPU can help you develop skills in various fields like problem-solving, development, and robotics. Therefore, it might be the best choice for you")

    elif any(word in query for word in Q2 ):
      speak("I'm Americano, an AI assistant created by senior members of CPU club. I can understand and reply to natural language, and I can also handle various tasks to help facilitate your life")

    elif any(word in query for word in Q3):
      speak("I'm gonna present all senior members of CPU club the president koussay attaya and his Vise Yosra ghanmi , SG Oumayma Badis , The RF are Aziz Harzallah and Mazen Tora , The RT Aya hosni , The RH  Mouna Dhaouad , The Treadurer  Skander sghaier , committee chef off-road  Jawher ben sousia , committee chef Fighter Mouhib ghanmi , committee chef junior Khadija elloumi , committee chef Autonome Najah zroud  , committee chef Logistics Fatma salama , committee chef media Tasnim Zroud , committee chef External matter Ranim radhouani , committee chef Design Ahmed mecrchaoui , committee chef sponsoring Yassine mthioueb")

    elif "open" in query:
      from engine.features import openCommand
      openCommand(query)

###################################

    elif "cyberbot" in query: 
      def speak_thread():
          speak("Isimm Cyberbot is a competition organized by CPU ISIMM club where competitors will have 4 challenges where they will choose one of them to play and win a prize. The first challenge, which is autonomous, requires autonomous robots that use sensors to follow a line and avoid obstacles. The second challenge is junior, oriented to children aged under 18, where they have a 4-wheel robot controlled with a remote control device, and the goal is to reach the finish line. The third challenge is the masterpiece, which is the All-terrain challenge, similar to junior but with older competitors and a bigger map. The final challenge is named fighter, where two robots are placed in a closed and secure ring to fight and destroy each other.")

      def video_thread():
          showvideo()

      # Create two threads
      speak_thread = threading.Thread(target=speak_thread)
      video_thread = threading.Thread(target=video_thread)

      # Start both threads
      speak_thread.start()
      video_thread.start()

      # Wait for both threads to complete
      speak_thread.join()
      video_thread.join()
      
    elif "on youtube" in query:
      from engine.features import playYoutube
      playYoutube(query)
    elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takeCommand()
                print(preferance)

                if "mobile" in preferance.lower():
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takeCommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "what" in preferance.lower():
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takeCommand()
                                        
                    elif "phone call" in query:
                        print("calling ")
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
              
                       
    else:
      from engine.features import chatBot
      chatBot(query)

  except Exception as error:
    # handle the exception
    print("An Error occurred:", error)

  eel.ShowHood()

