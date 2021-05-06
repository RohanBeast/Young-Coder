import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    colorhsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    colorhls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
    colorlab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    cv2.imshow("Camera Capture", colorhsv)
    cv2.imshow("Camera Capture 2", colorhls)
    cv2.imshow("Camera Capture 3", frame)
    cv2.imshow("Camera Capture 4", colorlab)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()