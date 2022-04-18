# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:06:20 2022

@author: Sourav Saha
"""
from nltk import sent_tokenize, word_tokenize
import pytesseract
import os
from pdf2image import convert_from_path
from date_class import date_class

# converting a scanned file to text
def scanned_file_to_text(file_path):
    doc = convert_from_path(file_path,500,poppler_path=r'C:\poppler-0.68.0\bin')
    path,fileName = os.path.split(file_path)
    fileBaseName,fileExtension = os.path.splitext(fileName)
    fl = open('input.txt','w')
    for page_number,page_data in enumerate(doc):
        txt = pytesseract.image_to_string(page_data).encode("utf-8")
        txt_2 = txt.decode('utf-8')
        fl.write(txt_2)
    fl.close()
    fl = open('input.txt','r')
    text = fl.read()
    fl.close()
    print('PDF to Text is done \n')
    return text

text=scanned_file_to_text("./Document.pdf")
sentences=sent_tokenize(text)
for sentence in sentences:
    formt = date_class(sentence,path = './date_pattern.txt')
    result = formt.date_extract()
    words=word_tokenize(sentence)
    for word in words:
        if result == 'yes':
            print('The date format ('+word+') is correct and is extracted by:\n'+formt)
            print(result)

