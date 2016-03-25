# coding: utf-8
#!/usr/bin/python


import sys 
import numpy as np
from parse import finalDicoTheme
from stemmingDico import newDico

def finalDico():
	X = []
	Y = []
	for element in os.listdir('/dico_racine'):
...     if element.endswith('.txt'):
		   descriptor = element[:-4]
		   newDico(element)
		   X1, Y1 = finalDicoTheme(element, descpritor)
		   X += X1
		   Y += Y1 
		   
	return X, Y	   



