# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:06:20 2022

@author: Sourav Saha
"""
from nltk import sent_tokenize, word_tokenize
from date_class import date_class

# Reading text file
fl = open('input.txt','r')
text = fl.read()
fl.close()

sentences = sent_tokenize(text)
for sentence in sentences:
    formt = date_class(sentence,path = './xyz/home/date_pattern.txt')
    result = formt.date_extract()
    words = word_tokenize(sentence)
    for word in words:
        if result == 'yes':
            print('The date format ('+word+') is correct and is extracted by:\n'+formt)
            print(result)

