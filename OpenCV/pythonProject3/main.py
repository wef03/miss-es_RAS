#bibliotecas
import cv2
import numpy

#parte 1
img = cv2.imread('passaro.jpg')

print('Largura em pixels: ', end='')
print(img.shape[1]) #largura do quadro
print('Altura em pixels: ', end='')
print(img.shape[0]) #altura do quadro
print('Qtde de canais: ', end='')
print(img.shape[2])


cv2.imshow("Nome da janela", img)
cv2.waitKey(0)
cv2.imwrite("saida.jpg", img)


#parte 2

print('De qual pixel você quer os valores RGB?')
a=int(input('Cite o número da linha do pixel:'))
b=int(input('Cite o número da coluna do pixel:'))

imagem = cv2.imread('passaro.jpg')
(b,g,r) = imagem[a,b]

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

#fim