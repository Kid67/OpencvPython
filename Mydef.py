import cv2

def import_img():
    path = input("Entrez le nom de l'image : ")
    img = cv2.imread(path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Output", img)
    cv2.imshow("Gray", imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


