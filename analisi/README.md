Abbiamo analizzato 11 curriculum, di cui abbiamo creato un file CSV
Informazioni sull’estrazione dei dati e creazione del file CSV.
Abbiamo preso in esempio 12 curriculum, da essi abbiamo recuperato dei dati sensibili che sono:
Nome - Cognome
Numero di telefono
Email
Nazionalità
Sex
Data di nascita
Religione
Indirizzo
All’interno del file CSV abbiamo inserito i dati recuperati in stile tabella, inserendo le     varie tuple in colonna. 
Abbiamo notato che nei documenti analizzati il dato nome e cognome è presente in quasi tutti (tranne uno) essendo presente il tag name che ci ha permesso di identificare il suddetto dato. Il problema è sorto solo in unico pdf (Numero 10) dove non è presente il tag name ma il nome e cognome viene inserito direttamente dalla persona interessata. I tag che abbiamo individuato sono:
Full Name
Name
NAME
Per quanto riguarda il numero di telefono abbiamo notato che anche esso è presente in tutti i curriculum, ma nel caso del PDF numero 2 e numero 6, la persona interessata ha inserito due numeri di telefono. I tag che abbiamo individuato sono:
Phone (Abbiamo utilizzato l’abbreviazione Ph e ph)
phone (Abbiamo utilizzato l’abbreviazione Ph e ph)
Contact
MOBNO
Per quanto riguarda l’email anche esso è presente in tutti i curriculum che abbiamo analizzato, tutti hanno un email in formato standard composta dal nome.cognome@dominio.it/com. Per individuare le mail presenti all’interno dei curriculum abbiamo inserito la parola “@” che ci ha permesso di individuare la mail della persona interessata
Per quanto riguarda la nazionalità in alcuni curriculum non è sempre presente. Abbiamo notato differenziazioni tra di loro poiché nel curriculum (2-3-8-10) non è presente il dato, in alcuni non abbiamo il tag nazionalità mentre in altri esso viene inserito all’interno del campo indirizzo. Per l’individuazione abbiamo utilizzato il tag
Nationality
Per quanto riguarda il genere in alcuni curriculum non è sempre presente. Abbiamo notato differenziazioni tra di loro poiché nel curriculum (2-3-8-11) non è presente il dato. Per l’individuazione abbiamo utilizzato il tag
Sex
Gender
Per quanto riguarda la data di nascita in alcuni curriculum non è sempre presente. Abbiamo notato differenziazioni tra di loro poiché nel curriculum (2-3) non è presente il dato. In alcuni viene inserito il formato yyyy-mm-dd mentri in altri il nome del mese. Per l’individuazione abbiamo utilizzato il tag
Birth
birth
Per quanto riguarda la religione abbiamo notato che solo in alcuni curriculum è presente (4-6-11) mentre in altri non è presente. Per l’individuazione abbiamo utilizzato il tag
Religion
Per quanto riguarda l’indirizzo in alcuni curriculum non è sempre presente. Abbiamo notato differenziazioni tra di loro poiché nel curriculum (1-4-6-11) non è presente il dato. In alcuni non abbiamo il tag address mentre in altri esso viene inserito insieme al nome e cognome, come titolo del curriculum. Per l’individuazione abbiamo utilizzato il tag
ADDRESS
address

Per sistema operativo windows per far eseguire l'OCR, installare il tesseract.exe e aggiungere la seguente linea di codice
-pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
sotto la riga 27.
Abbiamo inserito i curriculum in formato in pdf analizzati, all'interno dell'archivio zip di nome versione2.
Modificare i vari PATH.
