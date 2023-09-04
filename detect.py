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

    p3 =  [290, 717]  # 좌상
    p4 =  [570, 500] # 좌하
    p1 =  [720, 500] # 우상
    p2 = [1000, 717]  # 우하

    # corners_point_arr는 변환 이전 이미지 좌표 4개 
    corner_points_arr = np.float32([p1, p2, p3, p4])
    height, width = t_frame.shape[:2]


    image_p1 = [0, 0]
    image_p2 = [width, 0]
    image_p3 = [width, height]
    image_p4 = [0, height]

    image_params = np.float32([image_p1, image_p2, image_p3, image_p4])

    mat = cv2.getPerspectiveTransform(corner_points_arr, image_params)
    # mat = 변환행렬(3*3 행렬) 반
    image_transformed = cv2.warpPerspective(t_frame, mat, (width, height))

    cv2.namedWindow("Bird_Eye View", cv2.WINDOW_KEEPRATIO)
    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)

    cv2.imshow("Bird_Eye View", image_transformed)
    cv2.resizeWindow("Bird_Eye View", h, w)

    cv2.imshow('Frame', t_frame)
    cv2.resizeWindow("Frame", h, w)

    key = cv2.waitKey(13) 
    if key == 27:
        break   
    
cap.release()
cv2.destroyAllWindows()