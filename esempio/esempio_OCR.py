import pytesseract
import os

for img in ['Image.jpeg','Code.png','Excel.png']:
    script=img.split('.')[0]+'.txt'
    open(script, 'w').close
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

    text = pytesseract.image_to_string(img)
    with open(script, 'a') as f:
        f.write(text)