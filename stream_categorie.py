# coding: utf-8
#corpus=['Rendez-vous au Boogie Spirit Festival ce weekend à Illkirch','Samedi 6 Février, à la ComedieFr pour voir "La Double inconstance" de Marivaux!','Toujours personne pour le 104paris ce soir ? Une pièce pleine d\'humour qui mêle théâtre et danse, ça ne vous dit pas ?','Pour les fans de réécritures de contes, ne manquez pas ‘The Forbidden Wish’ le 23 février prochain!']

import time
from tweepy_import import FilteredStream

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from get_categorie import get_categorie_
import nltk
from nltk.corpus import stopwords
import preprocessor as p
from preprocess import set_sentence
from user_categories import user_categories_ as usr_cat

user_cat=usr_cat()
Nocat="Halloween"

np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

class MyFilteredStream(FilteredStream):
    def __init__(self):

        self.corpus = []
        self.new_cat = user_cat

        self.criterias = {
            "track": user_cat,
            "locations": [-0.6389644,44.8111222,-0.5334955,44.9163535],
            "lang": ["fr"]
        }
        FilteredStream.__init__(self, self.criterias, 10, "config.json")

    def action(self, tweets_list):
        for t in tweets_list:
            tweet = t["text"]
            tweet = p.clean(tweet.encode("utf-8"))
            #tweet = set_sentence(tweet.encode("utf-8"))

            s=get_categorie_([tweet])[0]
            if (s != Nocat):
                t["cat"]=s.encode("utf-8")
                t["text"] = t["text"].encode("utf-8")
                self.corpus.append(t)
                print tweet
                print t

    def get_corpus(self):
        r = []
        for t in self.corpus:
            r += [t]
        return r

    def clear_corpus(self):
        self.corpus = []

    def get_new_categories(self):
        r = []
        for t in self.new_cat:
            r += [t]
        self.new_cat = []
        return r

stream = MyFilteredStream()
stream.stream()
