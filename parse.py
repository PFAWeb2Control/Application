# coding: utf-8
#!/usr/bin/python


import sys 
import numpy as np



def insertChar(mystring, chartoinsert):
    position = len(mystring)
    mystring   =  mystring[:position] +" "+ chartoinsert + mystring[position:] 
    return mystring  

def finalDicoTheme(file, descprition):
    my_list = []
    my_list_categorie = []
    file =  "dico_racine/" + file 
    fichier = open(file, "r")
    i = 0
    toutesleslignes = fichier.readlines()
    for ligne in toutesleslignes:
        words = ligne.split(" ")
    for w in words:
        w = w.decode("utf-8")
        print w
        if(w.istitle()):
            i += 1
            my_list.append(w)

        if(w.islower()):
            print "if"
            w
            my_list[i-1] = insertChar(my_list[i-1], w)
    l = ["Architecture"]
    n = len(my_list) 
    my_list_categorie = [l]*n  


    fichier.close()  
    print my_list
    print my_list_categorie
    return my_list, my_list_categorie




        

