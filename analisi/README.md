Informazioni sull’estrazione dei dati e creazione del file CSV.
Abbiamo analizzato 3455 curriculum, essi sono stati divisi in due cartelle:
Funzionanti (443 curriculum)
Senza-Tag (3012 curriculum)
Abbiamo preso in considerazione quelli presenti nella cartella funzionanti, poiché provvisti di tag. Da loro abbiamo recuperato dei dati sensibili che sono:
Nome - Cognome
Numero di telefono
Email
Nazionalità
Sex
Data di nascita
Religione
Indirizzo
Nome del padre
Nome della madre
Lavoro
All’interno del file CSV abbiamo inserito i dati recuperati in stile tabella, inserendo le varie tuple in colonna. 
Abbiamo inserito all’interno della cartella “Senza-Tag” i curriculum dove mancavano tag:
Name
Address
Number.
…
Dove non era possibile recuperare da essi informazioni senza l’ausilio di algoritmi di Machine Learning.
I tag che sono stati utilizzati per la ricerca del nome sono i seguenti:
NAME
I tag che sono stati utilizzati per la ricerca dei numeri di telefono sono i seguenti:
PH
CONTACT
MOBNO
MOB
MOBILE NO
TEL
CELL
HP
Per quanto riguarda l’email anche esso è presente in tutti i curriculum che abbiamo analizzato, tutti hanno un email in formato standard composta dal nome.cognome@dominio.it/com. Per individuare le mail presenti all’interno dei curriculum abbiamo inserito la parola “@” che ci ha permesso di individuare la mail della persona interessata
I tag che sono stati utilizzati per la ricerca della nazionalità sono i seguenti:
NATIONALITY
I tag che sono stati utilizzati per la ricerca del sesso sono i seguenti:
SEX
GENDER
I tag che sono stati utilizzati per la ricerca della data di nascita sono i seguenti:
BIRTH
DOB
I tag che sono stati utilizzati per la ricerca della religione sono i seguenti:
RELIGION
I tag che sono stati utilizzati per la ricerca dell’indirizzo sono i seguenti:
ADDRESS
I tag che sono stati utilizzati per la ricerca del nome del padre sono i seguenti:
FATHER
I tag che sono stati utilizzati per la ricerca del nome della madre sono i seguenti:
MOTHER
Per analizzare i curriculum di linkedin, poichè la loro struttura è sempre uguale:
Il nome è presente prima del lavoro attuale ed il lavoro attuale prima dell’indirizzo.
Si è creato un metodo per ricercare l'indirizzo, tale ricerca è stata fatta per regione, per   	 
poi recuperare le due informazioni precedenti “Nome” e “Lavoro attuale”.
I tag utilizzati per questo metodo sono le regioni italiane.
