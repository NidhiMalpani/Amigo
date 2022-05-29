#MAIN FILE - COMBINED CODE OF ALL FILES WITH GUI

from tkinter import *
from tkinter import messagebox
# from tkinter import _Padding
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
# from requests import get
import wikipedia
import webbrowser
#import pywhatkit as kit
import pyautogui as p
from deepface import DeepFace
import random
import tkinter.font as tkFont
from PIL import Image
import numpy as np

#================================================================================================================#

user="Nidhi"

root = Tk()
root.geometry("2000x1500")
root.title("Face Recogniser")
bg = PhotoImage(file='bg4.png')
label1 = Label(root, image=bg)
label1.place(x=0,y=0, relwidth=1, relheight=1)

# canvas1 = Canvas( root, width = 1000, height = 1000)
# canvas1.pack(fill = "both", expand = True)

# canvas1.create_image( 0, 0, image = bg2, anchor = "nw")

#================================================================================================================#

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[1].id)

#================================================================================================================#

def write(txt):
    Label(root, text=txt).place(x=420, y=400, anchor=CENTER)

#----------------------------------------------

def speak(audio):       #Function to convert text to speech
    engine.say(audio)
    # print(audio)
    engine.runAndWait()     #Function that makes speech audible in the system

#----------------------------------------------

def spw(txt):          #speak-print-write
    speak(txt)
    print(txt)
    # write(txt)

#----------------------------------------------

def open(emotion):      #Opens the main command execution window of amigo
    p.press("esc")
    root1 = Toplevel()
    root1.title("Amigo")
    root1.geometry("2000x1500")
    label1 = Label(root1, image=bg)
    label1.place(x=0,y=0, relwidth=1, relheight=1)
    Label(root1, font=tkFont.Font(family="Vivaldi", size=50), text="Amigo", fg="White", bg="black", borderwidth=3, relief="sunken").place(x=100,y=100)
    Button(root1, text="Speak", font=tkFont.Font(family="Castellar",size=30), fg="White", bg="#141763", height=1, width=15, command=lambda: command_execution(emotion)).place(x=1300,y=500)
    Button(root1, text="Close", font=tkFont.Font(family="Castellar",size=30), fg="White", bg="#141763", height=1, width=15, command=root1.destroy).place(x=1300,y=700)

    # txt = lambda: command_execution(emotion)
    # if(txt == "stop"):
    #     root1.destroy

#----------------------------------------------

def new_user():     #Opens the window for adding new user - collecting samples and training the model
    p.press("esc")
    root2 = Toplevel()
    root2.title("Amigo")
    root2.geometry("2000x1500")
    label1 = Label(root2, image=bg)
    label1.place(x=0,y=0, relwidth=1, relheight=1)
    Label(root2, font=tkFont.Font(family="Vivaldi", size=50), text="Amigo", fg="White", bg="black", borderwidth=3, relief="sunken").place(x=100,y=100)
    Button(root2, font=tkFont.Font(family="Castellar",size=30), text="Take Samples", fg="White", bg="#141763", height=1, width=15, command=lambda: take_samples()).place(x=1300,y=500)
    Button(root2, font=tkFont.Font(family="Castellar",size=30), text="Model training", fg="White", bg="#141763", height=1, width=15, command=lambda: train_model()).place(x=1300,y=700)
    Button(root2, font=tkFont.Font(family="Arial", size=15), text="Back", fg="White", bg="#141763", command=root2.destroy).place(x=1700,y=900)

#----------------------------------------------

def take_samples():     #Takes photo samples of the new user
    camera=cv2.VideoCapture(0, cv2.CAP_DSHOW)      #To open internal camera
    camera.set(3, 640)      #Frame width
    camera.set(4, 480)      #Frame height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')        #prewritten xml file for effective object detection

    #user_id = int(input("Enter User Authentication ID: "))      #Different int IDs for different users
    print("Collecting samples. Please face the camera...")

    face_count=0

    while True:
        ret, img = camera.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #To make it easier for the model to understand
        faces = face_detector.detectMultiScale(gray_img, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)     #To draw a rectangle around the user's face
            face_count+=1

            #Creating jpg files of faces and writing them in dataset folder
            cv2.imwrite("dataset/sample."+str(face_count)+".jpg", gray_img[y:y+h,x:x+w])     
            cv2.imshow('Face',img)      #Display the face

        key = cv2.waitKey(100) & 0xff      #H(0xff) = Binary(11111111) = Decimal(255) -> to get integer below 255
        if key==27:     #Press 'Esc' key to stop
            break
        elif face_count>=20:    #Take 20 samples
            break
        else:
            continue

    spw("Samples collected successfully.")
    
    camera.release()
    cv2.destroyAllWindows()

#----------------------------------------------

def train_model():      #Trains the model based on given samples
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()      #Converts images to binary; LBP-Local Binary Pattern
    #It uses weighted LBPs and closest face is found using k-NN algorithm using chi sq distance
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")       #for effective detection

    path='dataset'

    def images(path):
        i_path = [os.path.join(path,file) for file in os.listdir(path)]
        samples=[]
        # face_ids = []
        label=[]
        # counter=1

        for i in i_path:
            gray_img = Image.open(i).convert('L')    #Converting to gray for easy detection
            img = np.array(gray_img,'uint8')    #8-bit integer 0-255
            
            # face_id= int(os.path.split(i)[-1].split(".")[1])
            faces=face_detector.detectMultiScale(img)

            for (x,y,w,h) in faces:
                samples.append(img[y:y+h,x:x+w])
                label.append(1)
                # face_ids.append(face_id)
        # print(face_ids)

            # no.append(counter)
            # counter+=1

        return samples, label

    print("Model training in progress...")

    # no=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # no=np.array(no)
    # for i in range(16):
    #     no.append(1)

    faces, label = images(path)
    # print(faces)
    # print(np.array(no))
    face_recognizer.train(faces, np.array(label))

    face_recognizer.write('model/trained_model.yml')
    spw('Model training successful.')

#----------------------------------------------

def face_recognition():         #Facial recognition - gives access to the main window of amigo
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()      #Converts images to binary; LBP-Local Binary Pattern
    face_recognizer.read('model/trained_model.yml')     #Load the trained model

    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

    camera=cv2.VideoCapture(0, cv2.CAP_DSHOW)      #To open internal camera
    camera.set(3, 640)      #Frame width
    camera.set(4, 480)      #Frame height

    win_width = int(0.1*camera.get(3))     #Min window width
    win_height = int(0.1*camera.get(4))    #Min window height

    while True:
        ret, img = camera.read()
        predictions = DeepFace.analyze(img, actions=['emotion'])
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #To make it easier for the model to understand
        faces = face_detector.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5, minSize=(win_width, win_height))

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)     #To draw a rectangle around the user's face

            label, accuracy = face_recognizer.predict(gray_img[y:y+h,x:x+w])

            if accuracy<100:
                name=user
                emotion = predictions['dominant_emotion']
                open(emotion)
                break
            else:
                name="unknown"
                speak("User authentication is failed")
                break

            accuracy="  {0}%".format(round(accuracy))
            
            font = cv2.FONT_HERSHEY_DUPLEX      #Font to be displayed
            cv2.putText(img, str(name), (x+5, y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (192,192,192), 1)

        cv2.imshow('Camera', img)

        key = cv2.waitKey(100) & 0xff      #H(0xff) = Binary(11111111) = Decimal(255) -> to get integer below 255
        if key==27:     #Press 'Esc' key to stop
            break
        else:
            continue

    print("Face recognition performed successfully.")

    camera.release()
    cv2.destroyAllWindows()

#----------------------------------------------

def start():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        txt = f"Good Morning, {user}"
    elif hour>12 and hour<16:
        txt = f"Good Afternoon, {user}"
    else:
        txt = f"Good Evening, {user}"
        
    spw(txt)
    spw("How may I help you?")
    # write("How may I help you?")

#----------------------------------------------

def recognise():      #Function to convert speech to text
    r=sr.Recognizer()
    with sr.Microphone() as source:     #Takes command from user using microphone
        spw('Say something...')

        try:
            r.pause_threshold=10     #So that the bot doesn't stop listening immediately when you take a pause
            audio=r.listen(source, timeout=5, phrase_time_limit=5)

        except Exception as e:
            spw("Took too long to respond, try again...")
            return "none"

    try:
        spw("Analyzing...")
        command=r.recognize_google(audio, language='en-in')    #Recognising user's speech
        print("User: ",command)

    except Exception as e:
        speak("Failed to recognise. Please speak again...")
        return "none"

    return command

#----------------------------------------------

def command_execution(emotion):     #Main amigo command-execution function
    p.press("esc")      #Pressing esc when we get verified
    speak("User verified.")
    speak(f'Emotion, {emotion}')
    start()

    while True:
    #if 1:
        command=recognise().lower()

        if "open camera" in command:
            #os.startfile("C:\Windows\System32\\camera.exe")
            capture=cv2.VideoCapture(0)     #0-internal camera; 1-external camera
            while True:
                ret, img = capture.read()
                cv2.imshow('Camera', img)
                wait_key = cv2.waitKey(50)      #Display window for 50 milliseconds
                if wait_key==27:        #Press 'Esc' to end
                    break
            capture.release()
            cv2.destroyAllWindows()

        elif "open calculator" in command:
            os.startfile("C:\Windows\System32\\calc.exe")

        elif "open notepad" in command:
            os.startfile("C:\Windows\System32\\notepad.exe")

        elif "open spotify" in command:
            os.startfile(r"C:\Users\Lenovo\AppData\Roaming\Spotify\Spotify.exe")

        elif "open youtube" in command:
            webbrowser.open("www.youtube.com")
            # speak("What do you want to play on youtube?")
            # video=recognise().lower()
            # kit.playonyt("see you again")

        elif "wikipedia" in command:
            command=command.replace("wikipedia","")
            summary=wikipedia.summary(command, sentences=1)
            speak("According to Wikipedia, ")
            spw(summary)

        elif "open google" in command:
            webbrowser.open("www.google.com")

        # elif "open command prompt" or "open cmd" in command:
        #     os.system("start cmd")

        elif "play music" in command:
            if emotion == "happy" or emotion == "neutral":
                songs_dir = 'happy_song'

            elif emotion == "sad":
                songs_dir = 'sad_song'
                
            else:
                songs_dir = 'soothing_song'
            
            songs = os.listdir(songs_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(songs_dir, song))

        elif "bye" in command:
            spw(f"Goodbye, {user}. Have a great day.")
            # root1.destroy
            break

        elif "stop" in command:
            break

    # return "stop"

    # recognise()
    # speak("Hello there")

#================================================================================================================#

# button2 = Button(root, text="Microphone", command=lambda: command_execution("happy")).pack()

label2 = Label(root, font=tkFont.Font(family="Vivaldi", size=50), text="Amigo", fg="White", bg="black", borderwidth=3, relief="sunken").place(x=100,y=100)
button2 = Button(root, font=tkFont.Font(family="Castellar",size=30), text="New User", fg="White", bg="#141763", height=1, width=15, command=new_user).place(x=1300,y=500)
button3 = Button(root, font=tkFont.Font(family="Castellar",size=30), text="Authenticate", fg="White", bg="#141763", height=1, width=15, command=lambda: face_recognition()).place(x=1300,y=700)

# def write(string,append=False):
#     if append:
#         text = label1.cget("text") + string
#         label1.configure(text=text)
#     else:
#         label1.configure(text=string)


# speak("Hello World")

# engine.say("Hello Nidhi my name is amigo")
# engine.runAndWait()

# root.wm_attributes("-transparentcolor", 'grey')

root.mainloop()