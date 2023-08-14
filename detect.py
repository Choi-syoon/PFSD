import cv2
import numpy as np

def roi(target):
    pts = np.array([[290, 717],[570, 500],[720, 500],[1000, 717]], np.int32)    # ROI 영역 지정
    mask = np.zeros_like(target)
    cv2.fillConvexPoly(mask, pts, (255,255,255))
    masked = cv2.bitwise_and(target, mask)
    return masked

def zeros_like(target, contours):
    task = np.zeros_like(target)
    cv2.drawContours(task, contours, -1, (0,255,0), 0)
    return task

video = input("Video Path : ")

h, w = (640, 360)

cap = cv2.VideoCapture(video)

while True:

    ret, t_frame = cap.read()
    
    gray = cv2.cvtColor(t_frame, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blurred, 100,100)
    roi_frame = roi(edges)
    view_frame = roi(blurred)
    contours, hierachy = cv2.findContours(roi_frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    zeros = zeros_like(t_frame, contours)
    cv2.drawContours(t_frame, contours, -1, (255,0,0), 0)
    
    cv2.namedWindow("Canny_Edges", cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)

    cv2.imshow("Canny_Edges", roi_frame)
    cv2.resizeWindow("Canny_Edges", h, w)

    cv2.imshow('Frame', t_frame)
    cv2.resizeWindow("Frame", h, w)

    key = cv2.waitKey(13) 
    if key == 27:
        break   
    
cap.release()
cv2.destroyAllWindows()