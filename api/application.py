'''
import numpy as np 
import pandas as pd 
import json
'''
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models import DB, Post
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
    @APP.route('/api', methods=['POST'])
    def make_predict(): # make prediction function
        post = request.get_json(force=True) # read in json data

        title = post['title']
        body = post['body']
        image = post['image'] #idk if we can/will do anything with this 

        text = title + " " + body
        text = re.sub(r'http\S+|www.\S+', 'link', text)
        text = list(text)

        def label_sentences(corpus, label_type):
            """
            Implementing Doc2Vec requires each body of text to have a label.
            We do this by using the TaggedDocument method. The format will be 
            "TRAIN_i" or "TEST_i" where "i" is a dummy index of the post.
            """
            labeled = []
            for i, v in enumerate(corpus):
                label = label_type + '_' + str(i)
                labeled.append(doc2vec.TaggedDocument(v.split(), [label]))
            return labeled
        def get_vectors(model, corpus_size, vectors_size, vectors_type):
            """
            Get vectors from trained doc2vec model
            :param doc2vec_model: Trained Doc2Vec model
            :param corpus_size: Size of the data
            :param vectors_size: Size of the embedding vectors
            :param vectors_type: Training or Testing vectors
            :return: list of vectors
            """
            vectors = np.zeros((corpus_size, vectors_size))
            for i in range(0, corpus_size):
                prefix = vectors_type + '_' + str(i)
                vectors[i] = model.docvecs[prefix]
            return vectors
    
        # prep text for prediction
        user_input = #need models to finish

        # predict, then convert to list for jsonify
        output = #need model to finish this

        # send back the top 5 subreddits and their associated probabilities
        return jsonify(top_five = output)
        '''



if __name__ == '__main__':
    APP.run(port = 5000, debug = True)