# coding: utf-8
import string
import sys 
from nltk.stem.snowball import FrenchStemmer
#from preprocess import Enleve_Accents


 ##################################################################
 #     intput_: original dictionary                               #
 #     output_: stemmed dictionary                                #
 #     example: python stemmingDico.py original.txt stemmed.txt   #
 ##################################################################
 
		
def Enleve_Accents(txt):
    ch1 = u"àâçéèêëîïôùûüÿ"
    ch2 = u"aaceeeeiiouuuy"
    s = ""
    for c in txt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s

def newDico(file):

	stemmer = FrenchStemmer()
	input_ = "dico_brut/" + file
	output_ = "dico_racine/" + file
	fs=open(input_,'r')
	fd=open(output_,'w')


	lines = fs.readlines()
	for line in lines:
		txt = line.split(" ")
		if txt =='':
			break
		for w in txt:
				
			w= w.decode("utf-8")
			w = ''.join(u for u in w if u in string.ascii_letters)
			w=Enleve_Accents(w)
			w=stemmer.stem(w)+" "
			w.encode("utf-8")
			fd.write(w)

	fs.close()
	fd.close()


newDico("architecture.txt")






