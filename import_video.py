import cv2

capture = cv2.VideoCapture("Ressources/test.mp4")

while True:
    success, img = capture.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyAllWindows()
