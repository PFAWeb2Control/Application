# coding: utf-8

X_sentence=[]
sentence1="un test"
sentence2="un test"

def X0sentence(corpus):
	X0_sentence=[]
	for sentence in corpus:
		sentence=[sentence]
		(X0_sentence.append(sentence))
	return X0_sentence

def Xsentence (corpus):
	X_sentence=[]
	corpus=list(corpus)
	for sentence in corpus:
		X_sentence.append(sentence)
	return X_sentence



	