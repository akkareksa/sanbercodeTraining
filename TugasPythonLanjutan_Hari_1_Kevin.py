# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:07:11 2020

@author: Kevin
"""

#1. Sebelumnya saya pernah melakukan percobaan Data Exploratory terhadap dataset review mie, melakukan percobaan machine learning, dll.
#2. Visualisasi, Machine Learning, dan pendalaman statistika dalam pengolahan data.
#3. 

class manipulasi:
    def __init__(self,data):
        self.data = data
        
    def upper_first(self):
        kata = self.data.lower().capitalize()
        print(kata)
    
    def lower_all(self):
        kata = self.data.lower()
        print(kata)
    
    def upper_all(self):
        kata = self.data.upper()
        print(kata)
    
    def split_string(self):
        split_list = self.data.split(' ')
        print(split_list)
    
    def solve(self):
        print('data = '+self.data)
        self.upper_first()
        self.lower_all()
        self.upper_all()
        self.split_string()
    
# Tester
manipulator = manipulasi("saya tinggal di Indonesia")
manipulator.solve()