import fitz
from unidecode import unidecode
import os
import pytesseract
import cv2
import csv

 
def lettura(file):
 text4=""
 doc = fitz.open(file)
 print()
 print("PDF Caricato Numero:")
 print(file)
 for page in doc:
    text =page.get_text()
    text1=unidecode(text)
    text4=text4+text1   
    if pdf_is_encrypted(file)==0: 
     if len(text1)==0:
      with fitz.open(file) as doc: 
       mat = fitz.Matrix(1.2, 1.2)
      pix = page.get_pixmap(matrix=mat)
      output = f'image/{page.number}.jpg'
      pix.save(output)
      img = cv2.imread(output)
      config = ('-l eng --oem 1 --psm 3')
      #pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
      text = pytesseract.image_to_string(img, config=config)
      text = text.split('\n')
      converted_list = map(str, text)
      result = ' '.join(converted_list)
      text4+=result
    
 return text4.upper()


def pdf_is_encrypted(file):
    pdf = fitz.Document(file)
    return pdf.isEncrypted

def decrypt_pdf(file):
    if pdf_is_encrypted(file):
        password = input('Enter pdf password : ')
        pdf = fitz.open(file)

        if pdf.authenticate(password):
            pdf.save('decrypted.pdf')
            dec=lettura('decrypted.pdf')
            if pdf.save:
                print("PDF decrypted")
                return dec
        else:
            print('Incorrect Password')


def creazionefile():
 with open('analisi/profiles2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Nome CV","nome-cognome", "telefono","Email","Nationality","Sex","Data-di-nascita","Religione","Indirizzo","Nome del padre","Nome della madre","Lavoro"]
    writer.writerow(field)
    file.close()
  
  
def estrazione2(file):
 i=0
 stringa = lettura(file).replace(":", "\n").replace(".","\n").replace("- ","\n").splitlines()
 while("" in stringa):
  stringa.remove("")
 x=len(stringa)
 nomecv=file
 nat=""
 nome="" 
 num=""
 mail=""
 sex=""
 data=""
 reli=""
 indi=""
 father=""
 madre=""
 lavoro=""
 emailTrovata=False
 nomeTrovata=False
 numTrovata=False
 natTrovata=False
 sexTrovata=False
 dataTrovata=False
 reliTrovata=False
 indiTrovata=False
 fathTrovata=False
 madreTrovata=False
 linkTrovata=False
 trova=False
  
 while(i<x):
  if('LINKEDIN' in stringa[i] and trova==False):
     nat=""
     nome="" 
     num=""
     mail=""
     sex=""
     data=""
     reli=""
     indi=""
     father=""
     madre=""
     lavoro=""
     nomeTrovata=True
     emailTrovata=True
     nomeTrovata=True
     numTrovata=True
     natTrovata=True
     sexTrovata=True
     dataTrovata=True
     reliTrovata=True
     indiTrovata=True
     fathTrovata=True
     madreTrovata=True
     trova=True
     if("@" in stringa[i-3]):
        mail=stringa[i-3]+"."+stringa[i-2]
          
  if(('GENOA' in stringa[i] or 'BENEVENTO' in stringa[i] or 'BERGAMO' in stringa[i] or 'ITALIA' in stringa[i] or 'CAGLIARI' in stringa[i] or 'PANARO' in stringa[i] or 'BOLOGNA' in stringa[i] or 'MILANO' in stringa[i] or 'LOMBARDIA' in stringa[i] or 'LAZIO' in stringa[i] or 'AVELLINO' in stringa[i] or 'UDINE' in stringa[i] or 'NAPOLI' in stringa[i] or 'BRESCIA' in stringa[i] or 'LOMBARDIA' in stringa[i]) or 'CAMPANIA' in stringa[i] or 'VENETO' in stringa[i] or 'SICILIA' in stringa[i] or 'EMILIA-ROMAGNA' in stringa[i] or 'PIEMONTE' in stringa[i] or 'PUGLIA' in stringa[i] or 'TOSCANA' in stringa[i] or 'CALABRIA' in stringa[i] or 'SARDEGNA' in stringa[i] or 'LIGURIA' in stringa[i] or 'MARCHE' in stringa[i] or 'ABRUZZO' in stringa[i] or 'FRIULI-VENEZIA-GIULIA' in stringa[i] or 'TRENTINO-ALTO ALGIDE' in stringa[i] or 'UMBRIA' in stringa[i] or 'BASILICATA' in stringa[i] or 'MOLISE' in stringa[i] or 'VALLE D`AOSTA' in stringa[i]):
          if(linkTrovata==False):
            nome=stringa[i-2]
            indi=stringa[i]
            lavoro=stringa[i-1]
            linkTrovata=True


  if('MOTHER' in stringa[i]):
          if("MR"in stringa[i+1]):
           if(madreTrovata==False):
            madre=stringa[i+2]
          else:
            madre=stringa[i+1]
          madreTrovata=True


  if('FATHER' in stringa[i]):
          if("MR"in stringa[i+1]):
           if(fathTrovata==False):
            father=stringa[i+2]
          else:
            father=stringa[i+1]
          fathTrovata=True

  if('ADDRESS' in stringa[i]):
          if(indiTrovata==False):
            c=i
            c=c+1
            while(True):
             if('DECLA' in stringa[c] or 'TELEPHONENO' in stringa[c] or 'PHONE' in stringa[c] or 'NATIONALITY' in stringa[c] or 'PERSONAL' in stringa[c] or 'MOBILE' in stringa[c] or 'MAIL' in stringa[c] or "PLACE" in stringa[c] or "(+91) 9441034015" in stringa[c]):
                break
             else:
              indi+=stringa[c]+" "
              indiTrovata=True
             
             c=c+1
            
             

  if('NATIONALITY' in stringa[i]):
          if(natTrovata==False):
            nat=stringa[i+1]
            natTrovata=True

  if('BIRTH' in stringa[i] or 'DOB' in stringa[i] ):
          if(dataTrovata==False and stringa[i+1]==' '):
            data=stringa[i+2]
            dataTrovata=True
          else:
            data=stringa[i+1]
            dataTrovata=True
  
  
  if('SEX' in stringa[i] or 'GENDER' in stringa[i]):
          if(sexTrovata==False):
            sex=stringa[i+1]
            sexTrovata=True

  if('RELIGION' in stringa[i]):
          if(reliTrovata==False):
            reli=stringa[i+1]
            reliTrovata=True
   
  if('@' in stringa[i]and emailTrovata==False):
        mail=stringa[i]+"."+stringa[i+1]
        emailTrovata=True        
  
  if( 'PH' in stringa[i] or "CONTACT" in stringa[i] or stringa[i]=="MOBNO" or "MOB" in stringa[i] or "MOBILE NO" in stringa[i] or "TEL" in stringa[i] or "CELL" in stringa[i] or "HP" in stringa[i]):
    if(stringa[i+1]==' ' and numTrovata==False):
     num=stringa[i+2]
     if(stringa[i+3].isdigit()):
        num+=stringa[i+3]
     numTrovata=True
    else:
      if(numTrovata==False):
       num=stringa[i+1]
       if(stringa[i+2].isdigit()):
        num+=stringa[i+2]
       numTrovata=True
  
  if(('NAME' in stringa[i])):
          if(nomeTrovata==False):
            nome=stringa[i+1]
            nomeTrovata=True
       
       
  i=i+1

 
 with open('analisi/profiles2.csv', 'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow([nomecv,nome, num,mail,nat,sex,data,reli,indi,father,madre,lavoro])
    f.close()




new_list=[]
for dirname, _, filenames in os.walk('pdf'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        new_list.append(os.path.join(dirname, filename))

file="CurriculumLinkedin/1.pdf"
#file="linkedin/AbbyTMiller.pdf"
#file=new_list[2000]
if pdf_is_encrypted(file):
 print(decrypt_pdf(file))
else:
 print(lettura(file))
 

       


creazionefile()
i=1
while(i<=443):
 estrazione2("analisi/Funzionanti/"+str(i)+".pdf") 
 i=i+1