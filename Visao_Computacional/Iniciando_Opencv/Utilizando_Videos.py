import cv2

video = cv2.VideoCapture(r'C:\Users\thiag\Desktop\Deep_Learning_Projects\Visao_Computacional\Iniciando_Opencv\Midias\runners.mp4')

while True:
    check, img = video.read()
    print(img.shape)
    imgRedin = cv2.resize(img, (640, 420))
    cv2.imshow('Video', imgRedin)
    cv2.waitKey(20)