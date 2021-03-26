try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np

imagem = Image.open('/home/leandro/Dev/covid19guaratingueta/20200619.jpg')

width, height = imagem.size 
  
# Setting the points for cropped image 
left = 100
top = 110
right = width - 400
bottom = 200
  
# Cropped image of above dimension 
# (It will not change orginal image) 
imagemCortada = imagem.crop((left, top, right, bottom))
#imagemCortada = imagemCortada.convert('LA')

print(pytesseract.image_to_string(imagemCortada, lang='por', config='-c tessedit_char_whitelist=0123456789 -oem 0'))  

# Shows the image in image viewer 
imagemCortada.save("/home/leandro/Dev/covid19guaratingueta/cortada.png")

npimagem = np.asarray(imagemCortada).astype(np.uint8)  
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

print(pytesseract.image_to_string(im, lang='por', config='-c tessedit_char_whitelist=0123456789 -oem 0'))

ret, thresh = cv2.threshold(im, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
binimagem = Image.fromarray(thresh) 
binimagem.save("/home/leandro/Dev/covid19guaratingueta/tresh.png")

print(pytesseract.image_to_string(binimagem, lang='por', config='-c tessedit_char_whitelist=0123456789 -oem 3'))


# import pytesseract as ocr
# import numpy as np
# import cv2

# from PIL import Image

# # tipando a leitura para os canais de ordem RGB
# imagem = Image.open('/home/leandro/Dev/covid19guaratingueta/20200619.jpg').convert('RGB')

# # convertendo em um array editável de numpy[x, y, CANALS]
# npimagem = np.asarray(imagem).astype(np.uint8)  

# # diminuição dos ruidos antes da binarização
# npimagem[:, :, 0] = 0 # zerando o canal R (RED)
# npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# # atribuição em escala de cinza
# im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

# # aplicação da truncagem binária para a intensidade
# # pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# # pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# # A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
# ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# # reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
# binimagem = Image.fromarray(thresh) 

# # chamada ao tesseract OCR por meio de seu wrapper
# phrase = ocr.image_to_string(binimagem)

# # impressão do resultado
# print(phrase) 