import pytesseract
import os

img=####path_to_image####
# le immagini possono essere in formato png/jpeg/jpg

script=####path_to_text####
# il file deve essere in formato .txt es: C:\Documenti\test.txt



open(script, 'w').close
pytesseract.pytesseract.tesseract_cmd = ####path_to_tesseract####
# es: /usr/local/Cellar/tesseract/4.1.1/bin/tesseract or 'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(img)
with open(script, 'a') as f:
    f.write(text)