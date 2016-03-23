# coding: utf-8
#!/usr/bin/python

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from twitter import *
from XX0 import *
from preprocess import set_sentence
from preprocess import Enleve_Accents


config = {}
execfile("config.py", config)


twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


def GenerateX_train(search):
	corpus=[]
	tmp=twitter.search.tweets(q = search,count=32000,lang="fr")
	for result in tmp["statuses"]:
		s=result["text"]
		s=str(s.encode("utf8"))
		s=str(set_sentence(s).encode("utf-8"))
		corpus.append(s)
	corpus=[corpus]
	return corpus

def GenerateY_train(X,label):
	Y_train=[]
	label=[label]
	for s in X:
		Y_train.append(label)
	return Y_train

X_train = np.array(["Politique politique politique","SPORT sport sport"])
                    
y_train_text0 = [["Politique"],["sport"]]


y_train_text = [x[0] for x in y_train_text0]
print y_train_text
           

X_test = np.array(["La politique est un sujet qui me passionne mais c'est compliqué sur internet","jaime le sport"])
target_names = ['Politique', 'Sport']
                   

lb = preprocessing.LabelBinarizer()
Y = lb.fit_transform(y_train_text)


classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, Y)
predicted = classifier.predict(X_test)
all_labels = lb.inverse_transform(predicted)

for item, labels in zip(X_test, all_labels):
    print '%s => %s' % (item,labels)