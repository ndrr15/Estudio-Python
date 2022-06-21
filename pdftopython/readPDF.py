from re import I
from PyPDF2 import PdfReader

from PIL import Image
import pytesseract
import tabula
import pandas as pd
import numpy as np
def read():
    
    # -------------------------------------------------------------------------
    file = "Declaraciones de Importación.pdf"
    # file = "DIM Febrero aperturas.pdf"
    # file = "DIM Febrero Renovaciones.pdf"

    # with open(file, 'rb') as fopen:
    # #     q = fopen.read()

    # df:list = tabula.read_pdf(file,pages = '2', multiple_tables = True)
    # print(df)
    # df = pd.DataFrame(np.array(df).reshape(4,11))
    # # for i in df:        
    # #     for j in df:
    # df.to_csv("prueba.csv", sep=";")
            
    # print(q)
    # -------------------------------------------------------------------------
    # f = open("Declaraciones de Importación.pdf", "rb")
    # print(f.read())
    # -------------------------------------------------------------------------
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    # print(number_of_pages)
    string=[]
    print(number_of_pages)
# ---------------------------------------------------------------------------------------------
    page_readed = reader.pages[1]
    _string:str = page_readed.extractText()
    string.append(_string.split('105.')[1].split('XXXXX')[0].split(' '))
    # string.append(_string.split('91.')[1].split('(continúa al respaldo')[0].split(' '))
# ---------------------------------------------------------------------------------------------
    
    # for page in range(0,number_of_pages) :
    #     print('# page',page)
    #     print('Length',len(string))
    #     page_readed = reader.pages[page]
    #     _string:str = page_readed.extractText()
        
    #     if _string.find('91.')>0:
    #         string.append(_string.split('91.')[1].split('(continúa al respaldo')[0].split(' '))
    #     else: 
    #         if _string.find('105.')>0:
    #             string.append(_string.split('105.')[1].split('XXXXX')[0].split(' '))


    
    


    # string=string.split('105.')[1].split('XXXXXXXXX')[0]

    print('----------------------------------------------------------------')
    print(string)
    print('----------------------------------------------------------------')
    # for index in string:
    #     _index=index.replace('\n','')

    #     if not _index.isalnum():
    #         print(_index)

    print('----------------------------------------------------------------')


   
read()
