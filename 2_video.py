import numpy as np
import cv2

cap = cv2.VideoCapture(0) # webcam

if cap.isOpened() == False:
    print('Cant find video capture')

while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
