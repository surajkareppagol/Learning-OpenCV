import cv2 as cv

# Images

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)

# Convert To Gray Scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Cat Grey", gray)

# Blur

blur = cv.blur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Cat Blur", blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating

dilate = cv.dilate(canny, (7, 7), iterations=5)
cv.imshow("Dilated", dilate)

# Eroding

erode = cv.erode(dilate, (7, 7), iterations=5)
cv.imshow("Eroded", erode)

# Resizing

resized = cv.resize(img, (320, 214), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Crop

crop = img[:, 480:]
cv.imshow("Cropped", crop)

if cv.waitKey(0) & 0xFF == ord("q"):
    cv.destroyAllWindows()
    exit()
