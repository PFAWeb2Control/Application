# coding: utf-8
#!/usr/bin/python


import sys 
import os
import numpy as np
from train_file import train_generate_with_roots
from stemming_dico import new_dico

def general_train():
	X = []
	Y = []
	for element in os.listdir('../dico/'):
		if element.endswith('.txt'):
			   descriptor = element[:-4]
			   new_dico(element)
			   X1, Y1 = train_generate_with_roots(element, descriptor)
			   X += X1
			   Y += Y1 

	return X, Y	   


#print general_train()