import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))
count = 0
while (True):
    success, img = cap.read()
    if success == True:
        #out.write(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Video stream", img)
        cv2.imshow("Video stream gray", gray)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('test%d.png' % count, img)
            count +=1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    else:
        break
cap.release()
cv2.destroyAllWindows()
