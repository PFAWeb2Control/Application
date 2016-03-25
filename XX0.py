# coding: utf-8
import sys 

########################################################
# 		prepare vectors for supervised                 #
#			   machine learning					       #
#		  python XX0.py categorie.txt categorie		   #
#													   #
########################################################
file=sys.argv[1]
def Xtrain():
	corpus=[]
	fs=open(file,"r")
	lines=fs.readlines()
	for line in lines:
		line=line.split()
		for word in line:
			corpus.append(word)
	fs.close()
	return corpus



def Ytrain():
	corpus=[]
	categorie=[sys.argv[2]]
	fs=open(file,"r")
	lines=fs.readlines()
	for line in lines:
		line=line.split()
		for word in line:

			corpus.append(categorie)
	fs.close()
	return corpus




