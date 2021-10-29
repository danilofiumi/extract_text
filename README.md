# extract_text

![ocrtest](https://user-images.githubusercontent.com/76904889/139340658-877bb2fe-9bb2-42d2-884e-12b22466b168.gif) <br>

Questa repo contiene il codice per estrarre qualsiasi tipo di testo da una qualsiasi immagine tramite Tesserract, l'OCR Open Source di Google.
<br>
 
## Installazione di Tesseract
Installare l'eseguibile Tesserac.

- Su MacOS <br>
`brew install tesseract `


- Su Windows10<br>
https://github.com/UB-Mannheim/tesseract/wiki


## Setup ed esecuzione su Python

Su Python, installare il pacchetto pytesseract.

`pip install pytesseract`



Aprire lo script *OCR_tesseract.py* e
sostituire i seguenti elementi:

1. **####path_to_image####** con il percorso dell' immagine della quale si vuole estrarre il testo. 
2. **####path_to_text####** con il percorso dove si vuole salvare lo script che conterrà il testo estratto dall' immagine <br> (es: C:\Documenti\test.txt)
3. **####path_to_tesseract####** il percorso all' eseguibile di Tesseract <br>
(es: /usr/local/Cellar/tesseract/4.1.1/bin/tesseract o 'C:\Program Files\Tesseract-OCR\tesseract.exe')

Eseguire il codice.



## Use case 
Nella cartella esempio ci sono 3 immagini con i rispettivi file testuali convertiti con lo script esempio_OCR.py.
Le immagini supportate dal motore OCR sono tutte quelle in formato png/jpeg/jpg.

## Idee di miglioramento
è possibile migliorare la conversione utilizzando dei metodi di pre-processing delle immagini, tramite i pacchetti `PIL` e `cv2`. Ad esempio:

- ridimensionare l'immagine in modo da aumentare la leggibilità <br>
`im_resized = im.resize((1980, 1000), Image.ANTIALIAS)`

- impostare un threshold ben calibrato (tendenzialmente infatti gli OCR lavorano meglio con immagini bianco e nero) <br>
`ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)`

## Reference
https://github.com/tesseract-ocr/tesseract
