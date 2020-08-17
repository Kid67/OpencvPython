import cv2

stream = cv2.VideoCapture(0)
stream.set(3, 640)
stream.set(4, 480)
stream.set(10, 100)

while True:
    success, img = stream.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



