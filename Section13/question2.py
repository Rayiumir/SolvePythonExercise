# 2. پخش ویدئو به صورت قاب به قاب:

import cv2

video = cv2.VideoCapture("1.mp4")  # جایگزین با مسیر ویدئو خود

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video Frame", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()