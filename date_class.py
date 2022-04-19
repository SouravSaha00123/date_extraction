# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:25:16 2022

@author: Sourav Saha
"""
import re

class date_class():
    def __init__(self,sentence='',path='./xyz/home/date_pattern.txt'):
        self.sentence = sentence
        self.path = path        
    
    def date_extract(self):
        fl=open(self.path,'r')
        patterns=fl.read().strip('\n').split('\n') 
        fl.close()
        dates=[]
        for pattern in patterns: 
            # results= re.findall(r""+pattern+"",sentence)
            results= re.findall(pattern,self.sentence) 
            if results:
               # print(results.group(0))
                dates.append(''.join(results[0])) 
                print(''.join(results[0]))            
                print(pattern)
         # input()
        return dates
