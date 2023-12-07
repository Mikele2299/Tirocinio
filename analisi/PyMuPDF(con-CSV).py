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
    
 return text4


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
    field = ["nome-cognome", "telefono","Email","Nationality","Sex","Data-di-nascita","Religione","Indirizzo"]
    writer.writerow(field)
    file.close()
  
def estrazione2(file):
 i=0
 stringa = lettura(file).replace(":", "\n").replace(".","\n").replace("- ","\n").splitlines()
 while("" in stringa):
  stringa.remove("")
 x=len(stringa)
 nat=""
 nome="" 
 num=""
 mail=""
 sex=""
 data=""
 reli=""
 indi=""
 emailTrovata=False
 nomeTrovata=False
 numTrovata=False
 natTrovata=False
 sexTrovata=False
 dataTrovata=False
 reliTrovata=False
 indiTrovata=False
 
  
 while(i<x):
  if('Address' in stringa[i] or 'ADDRESS' in stringa[i]):
          c=0
          if(indiTrovata==False):
            c=i
            c=c+1
            while(True):
             if('DECLARATION' in stringa[c] or 'TelephoneNo' in stringa[c] or 'Phone' in stringa[c] or 'NATIONALITY' in stringa[c] or 'Personal' in stringa[c] or 'Mobile' in stringa[c] or 'mail' in stringa[c]):
                break
             else:
              indi+=stringa[c]+" "
              indiTrovata=True
             
             c=c+1
            
             

  if('Nationality' in stringa[i]):
          if(natTrovata==False):
            nat=stringa[i+1]
            natTrovata=True

  if('Birth' in stringa[i] or 'birth' in stringa[i]):
          if(dataTrovata==False):
            data=stringa[i+1]
            dataTrovata=True
  
  if('Sex' in stringa[i] or 'Gender' in stringa[i]):
          if(sexTrovata==False):
            sex=stringa[i+1]
            sexTrovata=True

  if('Religion' in stringa[i]):
          if(reliTrovata==False):
            reli=stringa[i+1]
            reliTrovata=True
   
  if('@' in stringa[i]and emailTrovata==False):
        mail=stringa[i]+"."+stringa[i+1]
        emailTrovata=True        
  
  if( 'ph' in stringa[i] or 'Ph' in stringa[i] or "Contact" in stringa[i] or stringa[i]=="MOBNO" or "Mob" in stringa[i]):
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
  
  if((stringa[i]=="FullNames" or 'Name' in stringa[i] or 'NAME' in stringa[i])):
          if(nomeTrovata==False):
            nome=stringa[i+1]
            nomeTrovata=True
       
       
  i=i+1
 with open('analisi/profiles2.csv', 'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow([nome, num,mail,nat,sex,data,reli,indi])
    f.close()




new_list=[]
for dirname, _, filenames in os.walk('pdf'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        new_list.append(os.path.join(dirname, filename))

#file="scansmpl.pdf"
#file="Profile_protected.pdf"
file=new_list[2000]
if pdf_is_encrypted(file):
 print(decrypt_pdf(file))
else:
 print(lettura(file))
 

       


creazionefile()
estrazione2("analisi/versione2/1.pdf") 
estrazione2("analisi/versione2/2.pdf")
estrazione2("analisi/versione2/3.pdf")
estrazione2("analisi/versione2/4.pdf")
estrazione2("analisi/versione2/5.pdf")
estrazione2("analisi/versione2/6.pdf")
estrazione2("analisi/versione2/7.pdf")
estrazione2("analisi/versione2/8.pdf")
estrazione2("analisi/versione2/9.pdf")
estrazione2("analisi/versione2/10.pdf")
estrazione2("analisi/versione2/11.pdf")