# coding: utf-8
#!/usr/bin/python

import sys 
import numpy as np

"""
def insertChar(mystring, chartoinsert):
    position = len(mystring)
    mystring   =  mystring[:position] +" "+ chartoinsert + mystring[position:] 
    return mystring  
"""

#Generate the X, and the appropriate Y for the supervised training
def  train_generate_with_roots(file, descpritor):
    my_list = []
    my_list_categorie = []
    file =  "dic_with_roots/" + file 
    fichier = open(file, "r")
    i = 0
    k = 0
    toutesleslignes = fichier.readlines()
    for ligne in toutesleslignes:
        words = ligne.split(" ")
    for w in words:
        w = w.decode("utf-8")
        my_list.append(w)

    l = [descpritor]
    n = len(my_list) 
    my_list_categorie = [l]*n  



    fichier.close()  
    return my_list, my_list_categorie



        

