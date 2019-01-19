import cv2
import time
import datetime

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    if key == 13:
        key = cv2.waitKey()
        if key == 43:
            print("Truth")
            cv2.imwrite("Truth/" + st + ".jpg", frame)
        if key == 45:
            print("Lie")
            cv2.imwrite("Lie/" + st + ".jpg", frame)

    if key == 27:  # exit on ESC
        break
cv2.destroyWindow("preview")
