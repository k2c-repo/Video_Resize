import cv2
# import numpy as np

cap = cv2.VideoCapture('test.mov')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi', fourcc, 5, (640, 360))

while True:
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow("A", frame)

        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        b = cv2.resize(frame, (640, 360), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
