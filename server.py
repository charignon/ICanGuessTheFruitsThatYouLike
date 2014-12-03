#!/usr/bin/env/python 
# -*- coding: utf-8 -*-
import os
from flask import render_template
from flask import Flask
from flask import request

import networkx
from ffnet import ffnet, mlgraph
from random import shuffle
import csv
import json 

app = Flask(__name__)
# Run the algorithm
@app.route("/run", methods = ['POST'])
def run():

    def formatPrediction(u):
        if (u>0.5):
            return 1
        else:
            return 0
    dat = json.loads(dict(request.form).keys()[0])
    dat["pgood"]["values"] = []
    dat["pbad"]["values"] = []
    good = set(dat["good"]["values"])
    none = set(dat["none"]["values"])
    bad = set(dat["bad"]["values"])
    data = get_all_fruits()
    train_input  = []
    train_target = []
    test_input = []
    for f in data:
        if f[0] in good:
            train_input.append(f[1:])
            train_target.append(1)
        elif f[0] in bad:
            train_input.append(f[1:])
            train_target.append(0)
        elif f[0] in none:
            pass
        else:
            test_input.append(f)            
    
    print len(test_input)
    # Run algorithm
    l = len(data[0])-1
    conec = mlgraph( (l,2,1)) 
    net = ffnet(conec)
    net.train_tnc(train_input, train_target, maxfun = 1000)
    ## Print the name of the fruits used for test 
    
    o = net.test([u[1:] for u in test_input], [0]*len(test_input),iprint=0)
    res = [formatPrediction(u[0]) for u in o[0]]

    dat["pgood"]["values"] = [ k[0] for i,k in enumerate(test_input) if res[i] == 1 ]
    dat["pbad"]["values"] = [ k[0] for i,k in enumerate(test_input) if res[i] == 0 ]
    return json.dumps(dat)
import os

@app.route('/js/<path:path>')
def static_proxy(path):
    return app.send_static_file(os.path.join('js', path))

def get_all_fruits():
    with open("fruits.csv","rb") as f:
        reader = csv.reader(f)
        all_fruits  = [row for row in reader]
        header = all_fruits[0]
        return all_fruits[1:]
   

TEST_SAMPLES = 10
# Request the full list of fruits name
@app.route("/list")
def list():
    data = get_all_fruits()
    shuffle(data)
    return json.dumps([k[0] for k in data[TEST_SAMPLES:]])

# Main route, serve the page
@app.route("/")
def hello():
    return render_template('main.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
