import cv2
import time
fire_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
+'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
c=0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x, y, w, h) in fire:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        print('Face is detected..!')
        c=c+1;
        time.sleep(0.2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27 or c==10:
        break
cap.release()
cv2.destroyAllWindows()