import cv2
import os

haar='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/haarcascade_frontalface_default.xml'
images='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/images'
aurin='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/images/aurin'
nameimg=0
path=os.path.join(images,aurin)
fcc=cv2.CascadeClassifier(haar)
webcam=cv2.VideoCapture(0)
for i in range(30):
    nameimg+=1
    boolvalue,img=webcam.read()
    img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=fcc.detectMultiScale(img_gray,1.2,5)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),3)
        cropped_img=img_gray[y:y+h,x:x+w]
        resized_img=cv2.resize(cropped_img,(200,200))
        cv2.imwrite(f'{aurin}/{nameimg}.png',resized_img)