import cv2

camera = cv2.VideoCapture(0)
camera.set(3,640) #Largura
camera.set(4, 420) #Altura
camera.set(10,200) #Brilho

while True:
    check, img = camera.read()

    cv2.imshow('WebCan', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break