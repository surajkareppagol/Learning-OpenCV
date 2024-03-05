import cv2 as cv

# Images

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()
