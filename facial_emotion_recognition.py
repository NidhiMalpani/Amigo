#RECOGNISES FACIAL EMOTION

import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# img = cv2.imread('happy boy.jpg')
# predictions = DeepFace.analyze(img)
# print(predictions)
# print(predictions['dominant_emotion'])

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = camera.read()        #Read one image from the videp
    predictions = DeepFace.analyze(img, actions=['emotion'])

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #To make it easier for the model to understand
    faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)     #To draw a rectangle around the user's face

    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, predictions['dominant_emotion'], (x+5, y-5), font, 1, (255,255,255), 2)
    cv2.imshow('Camera', img)

    key = cv2.waitKey(100) & 0xff      #H(0xff) = Binary(11111111) = Decimal(255) -> to get integer below 255
    if key==27:     #Press 'Esc' key to stop
        break
    else:
        continue

camera.release()
cv2.destroyAllWindows()