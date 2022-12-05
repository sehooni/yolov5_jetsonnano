import cv2

import numpy as np 

cap = cv2.VideoCapture(0)
num = 0
while True:
    ret,frame = cap.read()
    
    if ret:
        cv2.imshow('',frame)
        path = 'runs/img_' + str(num) + '.png'
        cv2.imwrite(path,frame)
        if cv2.waitKey(5000) & 0xFF==ord('q'):

            break
    num += 1
cap.release()
cv2.destroyAllWindows()
