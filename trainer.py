#TRAINS THE MODEL 

from cProfile import label
import cv2
import numpy as np
from PIL import Image
import os

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
print('Model training successful.')