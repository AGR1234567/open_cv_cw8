import cv2
import os

haar='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/haarcascade_frontalface_default.xml'
images='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/images'
aurin='C:/Users/shuvo/OneDrive/Documents/Aurin - Home/Python classes/practice/Open CV/cw/cw8,9/images/aurin'
path=os.path.join(images,aurin)
fcc=cv2.CascadeClassifier(haar)
webcam=cv2.VideoCapture(0)
for i in range(3000000):
    webcam.read()