#!/usr/bin/python2
# coding: utf8

from __future__ import unicode_literals
import simplejson as json
import random
import thread
import numpy as np

from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

import stream_categorie as sg
from stream_categorie import MyFilteredStream as FStream
# from stream_categorie import t as new_tweets
# from stream_categorie import user_cat as new_categories

user = "hixe33"
max_tweets = 30

# new_categories = sg.new_categories
# new_categories = get_cat()
categories = []
# new_tweets=[]
tweets=[]

Nocat="Halloween"
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
stream = FStream()
stream.stream()

# thread.start_new_thread(stream.stream(), ())

# def init():
#     global new_categories, new_tweets
#     test_cat = ['Food', 'Politics', 'Fun', 'Hats', 'Trolling', 'Video games', 'Economy']
#     new_tweets = []
#     for i in range(0, len(test_cat)):
#         new_categories += [{   "color": "#%06x" % random.randint(0, 0xFFFFFF),
#                                 "id": i,
#                                 "name": test_cat[i]}]
#
#     with open("tweets.json", 'r') as f:
#         lst = json.loads(f.read())
#         for i in range(0,20):
#             new_tweets += [lst['tweets'][i]]
#             new_tweets[i]["cat"] = new_categories[random.randint(0, 6)]
#             new_tweets[i]["author"] = "Hixe"
#             new_tweets[i]["author_id"] = user
#             new_tweets[i]["id"] = "711976556613267457"

@app.route('/')
@app.route('/<username>')
def index(username=user):
    return render_template('index.html', username=username)

@app.route('/switch', methods=['POST', 'GET'])
def switchUser():
    user = request.form['username']
    return redirect(url_for('index', username=user))

@app.route('/update_categories', methods=['POST', 'GET'])
def update_categories(json=True):
    global categories, stream

    new_categories = stream.get_new_categories()
    print("SWAG")
    print("new C : ")
    print(len(new_categories))
    print("----")
    for c in new_categories:
        print c
        categories += [{   "color": "#%06x" % random.randint(0, 0xFFFFFF),
                            "id": len(categories),
                            "name": c}]

    if json:
        return jsonify(result=categories)

@app.route('/update_tweets', methods=['POST', 'GET'])
def update_tweets(json=True):
    global tweets, max_tweets, stream, categories

    print(len(tweets))
    print("YOLO")
    print("new-t : ")
    print (len(stream.get_corpus()) )
    print("****")
    for nt in stream.get_corpus():
        print nt
        tweets += [nt]

        if len(tweets) > max_tweets:
            tweets.pop(0)

    stream.clear_corpus()

    print(tweets)

    if json:
        return jsonify(result=tweets)

    # if redirect:
    #     return redirect(url_for('index', username=user
    # return redirect(url_for('index', username=user))

if __name__ == '__main__':
    # init()
    thread.start_new_thread(app.run(), debug=True)
    # app.run()
