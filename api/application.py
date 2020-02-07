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
from flask_cors import CORS

def create_app():
    APP = Flask(__name__)
    CORS(APP)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(APP)


    @APP.route("/")
    def index():
        return "Hello team!"


    @APP.route('/predict', methods=['POST'])
    def predict(): #define a prediction function
        # Get input text from request body
        APP.logger.info("/predict started")
        body = request.get_json(force=True)
        text = body['text']

        # Run through model
        knnPickle = 'api/modelknn_pkl.sav'
        model, index_df, tfidf = pickle.load(open(knnPickle, 'rb'))
        APP.logger.info("/predict pickle loaded")
        dist, indices = model.kneighbors(tfidf.transform([text]).todense())
        APP.logger.info("/predict kneighbors completed")
        recommended_subreddits = [index_df.iloc[n]['subreddit'] for n in indices[0]]
        resp = {
            'subreddits': uniq(recommended_subreddits)[:3]
        }
        APP.logger.info("/predict sort of done")

        # give output to sender.
        return APP.response_class(
            response=json.dumps(resp),
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



def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


if __name__ == '__main__':
    APP.run(port = 5000, debug = True)
