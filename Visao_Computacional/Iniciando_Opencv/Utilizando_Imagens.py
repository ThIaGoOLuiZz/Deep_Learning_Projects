import cv2

img = cv2.imread(r'C:\Users\thiag\Desktop\Deep_Learning_Projects\Visao_Computacional\Iniciando_Opencv\Midias\farol.jpg') #LER IMAGEM
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img.shape) #MOSTRA O TAMANHO DA IMAGEM
print(imgCinza) #MOSTRA OS CODIGOS DOS PIXELS
cv2.imshow('imagem', img) #MOSTRAR IMAGEM
cv2.imshow('Imagem Cinza', imgCinza)
cv2.waitKey(0) #MANTER IMAGEM ABERTA