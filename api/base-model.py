import pandas as pd
import numpy as np 
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_splitfrom sklearn.linear_model import LogisticRegression
from sklearn import utils
from tqdm import tqdm
