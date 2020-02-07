'''
Opening statement! its 930pm on thursday and i dont have
 a vectorizer or working model to test with, but this is all my code 
'''

# first import all the necessities
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
from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer


def create_app():
    APP = Flask(__name__)
    CORS(APP)
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(APP)
    model = pickle.load(open(model_pkl, 'rb')) 
    vector = pickle.load(open(vector_pkl))
    nlp = pickle.load(open('en_core_web_md.pkl', rb))

    @APP.route("/")
    def index():
        return "Hello team!"
    
    @APP.route('/predict/<body>', methods=['POST'])
    def predict(): #define a prediction function
        body = body.str.replace
        tokenizer = Tokenizer(nlp.vocab)
        tokens = []
        """ Make them tokens """
        #stop words
        STOP_WORDS = nlp.Defaults.stop_words.union(['', ' ', '-', 'reddit', 'post'])
        tokens = []
        for doc in tokenizer.pipe(df['combo'], batch_size=500):    
            doc_tokens = []
            for token in doc: 
                if ((token.text.lower() not in STOP_WORDS) and 
                    (token.is_stop == False) and 
                    (token.is_punct == False) and 
                    (token.pos_ != 'PRON')):
                        doc_tokens.append(token.lemma_.lower())
            tokens.append(' '.join(doc_tokens))
            
        df['tokens'] = tokens
        tfidf = TfidfVectorizer(min_df=0.025, max_df=.98, ngram_range=(1,2))
        vec_text = tfidf.transform(user_input)
        output = model.predict(vec_text.todense())  

        # give output to sender.
        return jsonify({"response": output})
    

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