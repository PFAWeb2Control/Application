# coding: utf8

from __future__ import unicode_literals
import simplejson as json
import random

from flask import Flask
from flask import render_template
app = Flask(__name__)

user = "hixe33"

cat = ['Food', 'Politics', 'Fun', 'Hats', 'Trolling', 'Video games', 'Economy']
categories = []

for i in range(0, len(cat)):
    categories += [{    "name": cat[i],
                        "color": "#%06x" % random.randint(0, 0xFFFFFF)}]


tweets = []
with open("tweets.json", 'r') as f:
    t = json.loads(f.read())
for i in range(0,20):
    tweets += [t['tweets'][i]]
    tweets[i]["cat"] = categories[random.randint(0, 5)]
    tweets[i]["author"] = "Hixe"
    tweets[i]["author_id"] = user
    tweets[i]["id"] = "711976556613267457"

@app.route('/')
def index():
    print (tweets[0])
    return render_template('index.html', categories=categories, tweets=tweets)

if __name__ == '__main__':
    app.run()
