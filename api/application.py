<<<<<<< HEAD
import numpy as np 
import pandas as pd 
import json
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models import DB
import pickle
import re
import os
import sqlite3
import praw
import spacy
import sklearn


def create_app():
    APP = Flask(__name__)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(APP)


    @APP.route("/")
    def index():
        return "Hello team!"

    
    @APP.route('/predict', methods=['POST'])
    def predict(): #define a prediction function
        lines = request.get_json(force=True) # read in json data
        body = lines['body'] # get variable

        #deserialize model
        with open('test_model.pkl', 'rb') as mod:
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
        return APP.response_class(
            response=json.dumps(send_back),
            status=200,
            mimetype='application/json'
        )
    

    @APP.route('/test', methods=['GET', 'POST'])
    def test():
        if request.method == 'GET':
            return jsonify({"response": "Get Request Called"})
        elif request.method == 'POST':
            req_Json = request.get_json(force=True)
            name = req_Json['name']
            return jsonify({"response": "Hi " + name})
    return APP
    



if __name__ == '__main__':
    APP.run(port = 5000, debug = True)