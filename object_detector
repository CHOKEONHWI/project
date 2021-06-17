#tracking.py
import cv2
#from tracker import *

#객체 추적
#tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("sample.mp4")

#고정되어 있는 카메라
object_detector = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold= 150)
object_detector_2 = cv2.createBackgroundSubtractorMOG2(history=600, varThreshold= 150)
while  True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    print(height, width)
    # 관심영역 추출
    roi_1 = frame[0:360 , 200 : 780]
    roi_2 = frame[360:720, 200 : 780]
    # 객체 감지
    mask_1 = object_detector.apply(roi_1)
    _, mask_1 = cv2.threshold(mask_1, 254, 255, cv2.THRESH_BINARY)
    contour, _ = cv2.findContours(mask_1,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detection1 = []
    for cnt in contour:
        # 면적계산 및 작은 요소 제거
        area = cv2.contourArea(cnt)
        if area > 300:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0),2)
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi_1, (x,y), (x + w, y +h ), (0, 255, 0),3)
            detection1.append([x, y, w, h])
            print(x, y, w, h)
            #pass
        # elif area <50:
        #     cv2.drawContours(frame, [cnt], -1, (0, 255, 0),2)

    mask_2 = object_detector_2.apply(roi_2)
    _, mask_2 = cv2.threshold(mask_2, 254, 255, cv2.THRESH_BINARY)
    contour, _ = cv2.findContours(mask_2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detection2 = []
    for cnt in contour:
        # 면적계산 및 작은 요소 제거
        area = cv2.contourArea(cnt)
        if area > 600:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0),2)
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi_2, (x,y), (x + w, y +h ), (0, 255, 0),3)
            detection2.append([x, y, w, h])

            print(x, y, w, h)

    cv2.imshow("roi1", roi_1)
    cv2.imshow("roi2", roi_2)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask_1)
    cv2.imshow("Mask", mask_2)


    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
