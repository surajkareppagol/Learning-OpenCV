import cv2 as cv

# Resizing

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat - Without Resize", img)

scale = 0.75

width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
dimensions = (width, height)

img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
cv.imshow("Cat - With Resize", img)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()


# For Resizing Video Capture Use capture.set(3, width) And capture.set(4, height)
