import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

path = "Ressources/Vignes/vigne2.png"


img = cv2.imread(path)
print(img.shape)

imgB = cv2.imread(path)
imgR = cv2.imread(path)
imgG = cv2.imread(path)
imgBlack = cv2.imread(path)
imgBlur = cv2.GaussianBlur(img, (7,7),0)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgCanny = cv2.Canny(imgBlur,250,150)
imgCanny2 = cv2.Canny(imgBlur,250,150)
imgBlur2 = cv2.GaussianBlur(imgHSV, (7,7),0)

imgB[:,:,0] = np.zeros([img.shape[0], img.shape[1]])
imgR[:,:,1] = np.zeros([img.shape[0], img.shape[1]])
imgG[:,:,2] = np.zeros([img.shape[0], img.shape[1]])
imgBlack[:] = 0,0,0


imgStack = stackImages(0.5, ([img, imgGray, imgHSV, imgCanny,imgCanny2], [imgB, imgR, imgG, imgBlur, imgBlack]))


cv2.imshow("ImageStack", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()