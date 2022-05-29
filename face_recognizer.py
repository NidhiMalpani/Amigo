#CODE TO RECOGNISE FACE OF THE USER

import cv2

face_recognizer = cv2.face.LBPHFaceRecognizer_create()      #Converts images to binary; LBP-Local Binary Pattern
face_recognizer.read('model/trained_model.yml')     #Load the trained model

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 

user="Nidhi"

camera=cv2.VideoCapture(0, cv2.CAP_DSHOW)      #To open internal camera
camera.set(3, 640)      #Frame width
camera.set(4, 480)      #Frame height

win_width = int(0.1*camera.get(3))     #Min window width
win_height = int(0.1*camera.get(4))    #Min window height

while True:
    ret, img = camera.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #To make it easier for the model to understand
    faces = face_detector.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5, minSize=(win_width, win_height))

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)     #To draw a rectangle around the user's face

        label, accuracy = face_recognizer.predict(gray_img[y:y+h,x:x+w])

        if accuracy<50:
            name=user
        else:
            name="unknown"

        accuracy="  {0}%".format(round(100-accuracy))
        
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