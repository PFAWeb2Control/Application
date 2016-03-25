# coding: utf-8
import string
import sys 
from nltk.stem.snowball import FrenchStemmer
from preprocess import Enleve_Accents




 ##################################################
 #     intput_: original dictionary               #
 #     output_: stemmed dictionary                #
 #     example: python original.txt stemmed.txt   #
 ##################################################
 
stemmer = FrenchStemmer()
input_ = sys.argv[1]
output_ = sys.argv[2]
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







