#!/usr/bin/python2
# coding: utf8

from __future__ import unicode_literals
import simplejson as json
import random
import thread
import numpy as np
import argparse

args_parser = argparse.ArgumentParser(description='Simple application suggesting tweets with the help of Machine Learning algorithms')
args_parser.add_argument('pseudo', metavar='<pseudo>', type=str,
                   help='Twitter user\'s name (without the @)')
args = args_parser.parse_args()

from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

import stream_categorie as sg
from stream_categorie import MyFilteredStream as FStream

user = args.pseudo
max_tweets = 30 # Arbitrary maximum number of tweets

categories = []
tweets=[]

Nocat="Halloween" # Joker category
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
stream = FStream()
stream.stream()

"""
Simply show the index page
:param username: The user's name (simply esthetic for the moment)
"""
@app.route('/')
@app.route('/<username>')
def index(username=user):
    return render_template('index.html', username=username)

"""
Change the user (useless for the moment)
:param request.form['username']: New user's name
"""
@app.route('/switch', methods=['POST', 'GET'])
def switchUser():
    user = request.form['username']
    return redirect(url_for('index', username=user))

"""
Update the list of the categories
:param json: True if a return is required
:return: Returns the list of the categories (JSON format)
"""
@app.route('/update_categories', methods=['POST', 'GET'])
def update_categories(json=True):
    global categories, stream
    new_categories = stream.get_new_categories()

    for c in new_categories:
        categories += [{   "color": "#%06x" % random.randint(0, 0xFFFFFF),
                            "id": len(categories),
                            "name": c}]

    if json:
        return jsonify(result=categories)

"""
Update the list of the tweets
:param json: True if a return is required
:return: Returns the list of the tweets (JSON format)
"""
@app.route('/update_tweets', methods=['POST', 'GET'])
def update_tweets(json=True):
    global tweets, max_tweets, stream, categories

    for nt in stream.get_corpus():
        # Just in case the tweet's category has been removed for a mysterious reason
        has_cat = False

        for c in categories:
            if c["name"] == nt["cat"]:
                nt["cat"] = c
                has_cat = True

        if has_cat:
            tweets += [nt]

            if len(tweets) > max_tweets:
                tweets.pop(0)

    stream.clear_corpus()

    print(tweets)

    if json:
        return jsonify(result=tweets)

"""
Simply launche the app in a new thread
Set debug to True to activate the powerful Flask's debugger
"""
if __name__ == '__main__':
    # thread.start_new_thread(app.run(), debug=True)
    thread.start_new_thread(app.run(), debug=False)
