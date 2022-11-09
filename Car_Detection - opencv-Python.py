import cv2
import numpy as np
import imutils

alg="C:\\AI(ml&dl)\\DATASETS\\Vehicle_Detection\\cars.xml"
car_cascade=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0)

while True:
    detected=0
    _,img=cam.read()
    img=imutils.resize(img,width=300)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    b=str(len(cars))
    a=int(b)
    detected=a
    n=detected
    print('........................................................')
    print('North: %d'%(n))
    if n>=2:
        print('North More Traffic')
    else:
        print('No Traffic')

    cv2.imshow('Car',img)
    if cv2.waitKey(1)==1:
       break
cam.release()
cv2.destroyALLWindows()
          
