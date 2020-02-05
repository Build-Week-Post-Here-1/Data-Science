import numpy as np 
import pandas as pd 
import json
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models import DB
import pickle
'''
import gensim
import gensim.models.doc2vec as doc2vec
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import re
import os
from dotenv import load_dotenv
import sqlite3
import praw
'''
'''
import ml model here in this format
modeltype = pickle.load(open('#name of model#.pkl', 'rb'))
model_dbow = Doc2Vec.load('#doc2vector model#.pkl')


'''

def create_app():
    APP = Flask(__name__)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(APP)


    @APP.route("/")
    def index():
        return "Hello team!"

    return APP

    '''
    @APP.route('/predict', methods=['POST'])
    def predict(): #define a prediction function
        lines = request.get_json(force=True) # read in json data
        body = lines['body'] # get variable

        #deserialize model
        with open('model.pickle', 'rb') as mod:
            model = pickle.load(mod)

        #actual prediction
        output = model.predict([[body]])

        # use a dictionary to format output for json
        send_back = {'prediction': output}
        send_back_dummy = {'dummy': 1} # minimal functionality for testing
        send_back_input = { # verify that input is working as expected
            'body': body
            }
    
        # give output to sender.
        return app.response_class(
            response=json.dumps(send_back),
            status=200,
            mimetype='application/json'
        )
    '''



if __name__ == '__main__':
    APP.run(port = 5000, debug = True)