import cv2

video = cv2.VideoCapture()
ip = "{ip}:{porta}/video"
video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("Img", img)
    cv2.waitKey(1)