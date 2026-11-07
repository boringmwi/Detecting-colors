import numpy as np
from PIL import Image
import cv2 as cv

from utils import get_limits

green = [0, 255, 0] 
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerLimitG, upperLimitG = get_limits(color=green)

    maskG= cv.inRange(hsvImage, lowerLimitG, upperLimitG)

    maskG_ = Image.fromarray(maskG)

    bboxG = maskG_.getbbox()

    if bboxG is not None:
        x1, y1, x2, y2 = bboxG
            
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (50, 100, 50), 5)
            
    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        

cap.release()
cv.destroyAllWindows()
