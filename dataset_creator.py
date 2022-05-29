#Creates samples for "trainer.py" to train on

import cv2

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
    elif face_count>=15:    #Take 10 samples
        break
    else:
        continue

print("Samples collected successfully.")
camera.release()
cv2.destroyAllWindows()
