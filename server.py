#!/usr/bin/python2
# coding: utf8

from __future__ import unicode_literals
import simplejson as json
import random

from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

user = "hixe33"
max_tweets = 30

new_categories = []
categories = []
new_tweets=[]
tweets=[]

def init():
    global new_categories, new_tweets
    test_cat = ['Food', 'Politics', 'Fun', 'Hats', 'Trolling', 'Video games', 'Economy']
    new_tweets = []
    for i in range(0, len(test_cat)):
        new_categories += [{   "color": "#%06x" % random.randint(0, 0xFFFFFF),
                                "id": i,
                                "name": test_cat[i]}]

    with open("tweets.json", 'r') as f:
        lst = json.loads(f.read())
        for i in range(0,20):
            new_tweets += [lst['tweets'][i]]
            new_tweets[i]["cat"] = new_categories[random.randint(0, 6)]
            new_tweets[i]["author"] = "Hixe"
            new_tweets[i]["author_id"] = user
            new_tweets[i]["id"] = "711976556613267457"

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
    global new_categories, categories

    for c in new_categories:
        categories += [c]

    new_categories = []
    if json:
        return jsonify(result=categories)

@app.route('/update_tweets', methods=['POST', 'GET'])
def update_tweets(json=True):
    global new_tweets, tweets, max_tweets, categories

    for t in new_tweets:
        tweets += [t]

        if len(tweets) > max_tweets:
            tweets.pop(0)

    new_tweets = []
    if json:
        return jsonify(result=tweets)

    # if redirect:
    #     return redirect(url_for('index', username=user
    # return redirect(url_for('index', username=user))

if __name__ == '__main__':
    init()
    app.run(debug=True)
