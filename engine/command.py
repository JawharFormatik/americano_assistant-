import pyttsx3 #pick the voice 
import speech_recognition as sr
import eel
import time

@eel.expose
def speak(text):
  text = str(text)
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female 2 For male
  engine.setProperty('rate', 174)     # setting up new voice rate(voice speed)
  eel.DisplayMessage(text)
  eel.DisplayMessage(text)
  engine.say(text)
  eel.recieverText(text)
  engine.runAndWait()

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
     
  try:

    if "open" in query:
      from engine.features import openCommand
      openCommand(query)
    elif "club cpu" in query:
       from engine.features import showimages
       showimages()
    elif "cyberbot" in query: 
       speak("Isimm Cyberbot is a competition organized by CPU Isimm where competetors will have 4 challenges where they will chose one of them to play and win a prize , the first challenge which is autonomus , this autonomous challenge requires autonomous robots as the word says it is a robot based on sensors that hepls him to follow a line and avoid obsticals , the second challenge is junior it is a challenge oriented to children aged under 18 where they have a 4 wheel robot controlled with a remote controle device and the goal is to reach the finish line , as far as we go we have at the third place the master peace which is the challenge All terrain , it is the same as junior with older competetors and bigger map , running to the final challenge named as fighter , this challenge is a showcase of the power of destroying machines , two robots will be placed in a closed and secure ring to fight and destroy each other , for more explaination i will show you the last year video to know more about isimm cyberbot ")     
       from engine.features import showvideo
       showvideo()  
      
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







