import cv2

# UTILIZANDO SELEÇÃO DA IMAGEM
img = cv2.imread(r'C:\Users\thiag\Desktop\Deep_Learning_Projects\Visao_Computacional\Iniciando_Opencv\Midias\farol.jpg') #LER IMAGEM
dim = cv2.selectROI("SELECIONE A AREA DE RECORTE", img, False)
cv2.destroyAllWindows()
print(dim)
valor1 = int(dim[0])
valor2 = int(dim[1])
valor3 = int(dim[2])
valor4 = int(dim[3])


recorte = img[valor2:valor2+valor4, valor1:valor1+valor3]
diretorio = r'C:\Users\thiag\Desktop\Deep_Learning_Projects\Visao_Computacional\Iniciando_Opencv\Recortes'
nome_arquivo = input('Digite o nome do arquivo: ')
cv2.imwrite(f'{diretorio}\{nome_arquivo}.jpg', recorte)
print('Salvo com sucesso!')


# UTILIZANDO COORDENADAS PRONTAS
# recorte = img[310:520, 120:420]
# cv2.imshow('imagem', img) #MOSTRAR IMAGEM
# cv2.imshow('recorte', recorte) #MOSTRAR IMAGEM
# cv2.waitKey(0) #MANTER IMAGEM ABERTA

