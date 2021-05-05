import cv2 as cv
import numpy as np

thresh = 25
max_diff = 5

a, b, c = None, None, None

cap = cv.VideoCapture("http://192.168.219.31:8091/?action=stream")

if cap.isOpened():
    ret, a = cap.read()
    ret, b = cap.read()
    while ret:
        ret, c = cap.read()
        draw = c.copy()
        if not ret:
            break

        a_gray = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
        b_gray = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
        c_gray = cv.cvtColor(c, cv.COLOR_BGR2GRAY)

        diff1 = cv.absdiff(a_gray, b_gray)
        diff2 = cv.absdiff(b_gray, c_gray)

        ret, diff1_t = cv.threshold(diff1, thresh, 255, cv.THRESH_BINARY)
        ret, diff2_t = cv.threshold(diff2, thresh, 255, cv.THRESH_BINARY)

        diff = cv.bitwise_and(diff1_t, diff2_t)

        k = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
        diff = cv.morphologyEx(diff, cv.MORPH_OPEN, k)

        diff_cnt = cv.countNonZero(diff)
        if diff_cnt > max_diff:
            nzero = np.nonzero(diff)
            cv.rectangle(draw, (min(nzero[1]), min(nzero[0])), (max(
                nzero[1]), max(nzero[0])), (0, 255, 0), 2)

            cv.putText(draw, "Motion detected!", (10, 30),
                       cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        stacked = np.hstack((draw, cv.cvtColor(diff, cv.COLOR_GRAY2BGR)))
        cv.imshow('motion', stacked)

        # next frame
        a = b
        b = c

        if cv.waitKey(1) & 0xFF == 27:
            break