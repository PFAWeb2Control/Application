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







X_train = np.array(["Sur #Sarkozy : Il faut nettoyer le milieu politique, que ce qui sont mis en examen ou condamnés dégagent @Azizsenni "
					,"Actu. Politique - Le Maire, Cambadélis, Attali... Qui gagnera le Prix humour politique "
					,"Plusieurs politique paradent sur les plateaux pour proposer leur idée géniale : la perpétuité réelle pour les terroristes"
					,"La classe politique doit s'emparer de ce débat"
					,"Dans la presse algérienne les dessinateurs font de la politique. Et de la bonne. Autre chose que Plantu."
					,"Michel Sapin ose faire la leçon aux Belges à propos du communautarisme ?"
					,"Le refus de voir la réalité est permanent parmi la classe politique. Résultat, l'islamisme radical tue chaque jour un peu plus !"
					,"Explosions à Bruxelles : droite ou gauche, la récupération politique n'attend pas"
					,"La guerre contre le terrorisme est perdue d'avance, l'occident devrait revoir sa politique étrangère afin de minimiser les dégâts"
					,"Quand j'entends Valls (politique professionnel depuis 1983) dire à des ouvriers qu'il a un emploi précaire. "
					,"SPORT sport","Faut-il calquer la régulation du e-sport sur celle du secteur sportif ? Il y a encore des réticences..."
					,"j'interdirai de faire piscine en sport au lycée voilà"
					,"#Actu #Afrique : #Football, visite du président de la #FIFA au Soudan du Sud"
					,"Football : Italie / Espagne, à suivre en direct à 20h30"
					,"Paris sportifs : la cote d'alerte ? On ne compte plus les affaires de manipulations de matches liées aux paris sportifs. Dans le monde, 1 rencontre sur 100 est aujourd'hui suspecte. Les championnats français sont-ils à l'abri ?",
					"Valence est intéressé par Halilovic, le club souhaite le prêter une saison supplémentaire."
					," Les amendes des joueurs pour être arrivé en retard à un entraînement ou un match","Un retour de Benzema en équipe de France «choquerait» Martin Fourcade"
					," 1ère séance d'entrainement ","L'extorsion par piratage informatique en plein essor dans le monde "
					,"Le piratage informatique sous forme de rançon en plein essor dans le monde"
					,"Informatique : les entreprises où il est le plus agréable de travailler en France"
					,"Le marché de la sécurité informatique devrait franchir la barre de 200 millions en 2020"
					,"Adele victime d'un pirate informatique, des photos privées publiées sur Internet"
					,"J'ai créé un site dédié à Linux et à la sécurité informatique"
					,"Assistant Administratif et Commercial  Formateur en Bureautique et Informatique au service des Professionnels"
					,"Victime d’une attaque informatique, le site de Canal Plus inaccessible "
					,"Emploi Algofi : Ingenieur C++ Front-Office.+ Ingenieur/Bac+5 informatique","Vinci Facilities récompensé pour son portail de services http://buff.ly/1QQXdDu  #informatique #CloudComputing"
					,"dans les années 2000 t'avais pas une soiree sans cette musique ","De la Révolution française au Free Jazz, histoire de la musique et du pouvoir"
					,"La poésie est la musique des mots .","La danse et la musique c'est ce qu'il y a de mieux"
					,"La musique est le langage des émotions "
					,"En ondes / Now playing"])
                    
y_train_text0 = [["Politique"],["Politique"],["Politique"],["Politique"],["Politique"],["Politique"],["Politique"],["Politique"],["Politique"],["Politique"]
				,["sport"],["sport"],["sport"],["sport"],["sport"],["sport"],["sport"],["sport"],["sport"],["sport"]
				,["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],["informatique"],
				["musique"],["musique"],["musique"],["musique"],["musique"],["musique"]]

y_train_text = [x[0] for x in y_train_text0]

           

X_test = np.array(["La politique est un sujet qui me passionne mais c'est compliqué sur internet","jaime le football","le piratage internet","dormir en ecoutant la musique"])
target_names = ['Politique', 'Sport',"informatique","musique"]
                   

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
