# coding: utf-8
import string
import sys 
from nltk.stem.snowball import FrenchStemmer

#Function that remove the accent	
def enleve_accents(txt):
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

#generate file containing the roots of the words in the original file
def new_dico(file):
	stemmer = FrenchStemmer()
	input_ = "../dico/" + file
	output_ = "dic_with_roots/" + file
	fs=open(input_,'r')
	fd=open(output_,'w')

	k =0
	lines = fs.readlines()
	for line in lines:
		txt = line.split(" ")
		if txt =='':
			break
		for w in txt:
			if(w.istitle()):	
				k = 1
			else:
				k = 0	
			w= w.decode("utf-8")
			w = ''.join(u for u in w if u in string.ascii_letters)
			w=enleve_accents(w)
			w=stemmer.stem(w)+" "
			w.encode("utf-8")
			if(k):
				w = w[0].upper() + w[1:]
				fd.write(w)
			else:
				fd.write(w)

	fs.close()
	fd.close()








