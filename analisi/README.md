Abbiamo analizzato 11 curriculum, di cui abbiamo creato un file CSV
contenente il:
-Nome
-Cognome
-Email
-Numero di telefono
Per sistema operativo windows per far eseguire l'OCR, installare il tesseract.exe e aggiungere la seguente linea di codice
-pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
sotto la riga 27.
Abbiamo inserito i curriculum in formato in pdf analizzati, all'interno dell'archivio zip di nome versione2.
