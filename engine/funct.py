import cv2


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
    cv2.destroyWindow('ISIMM CyberBot V3.0')  

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
    resized_image12= cv2.resize(img12, (500, 400))
    resized_image13= cv2.resize(img13, (new_width2, new_height2))
    resized_image14= cv2.resize(img14, (new_width2, new_height2))

    speak("CPU Club at ISIMM was established in 2018 with a clear mission: to enhance students’ skills in development, problem-solving, and robotics. Through regular competitions and engaging projects, the club provides students with valuable opportunities to showcase their talents and put their skills to the test")
    speak("Here some pictures about last year integration day ")
    cv2.imshow('integration day',resized_image5)
    cv2.setWindowProperty("integration day", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('integration day')

    cv2.imshow('Team building day',resized_image6)
    cv2.setWindowProperty('Team building day', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('Team building day')

    cv2.imshow('Team building day2',resized_image1)
    cv2.setWindowProperty('Team building day2', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('Team building day2')
    
    
    speak("In addition the CPU activitis contains worckshops in the developpment and robotic domains  ")
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

    speak("as we see here our dev team had participated at the TCPC Competitions , it's an honor to see young talented students grwing up and moving forward")
    cv2.imshow('big pics',resized_image13)
    cv2.setWindowProperty('big pics', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)

    speak("however i will never forget the robotics competitions which is a place for competetive minds ")
    cv2.imshow('festival',resized_image14)
    cv2.setWindowProperty('festival', cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(delay=3000)
    cv2.destroyWindow('festival')
    cv2.destroyWindow('big pics')
    cv2.destroyWindow('cpu')


