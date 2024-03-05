import cv2 as cv

# Videos

# Pass Integer Value For Web Cam
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    read_success, frame = capture.read()
    cv.imshow("Dog", frame)

    # -215: Assertion Error

    """
  q    = 01110001
  0xFF = 11111111
        ----------
         01110001 -----> q so when do bitwise and operation we get the same value of q
  """

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
