import os
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer, CountVectorizer
import string
import time

import warnings 
warnings.filterwarnings("ignore")


fileDir = os.path.dirname(os.path.realpath('__file__'))

joblib_vect = pickle.load(open(os.path.join(fileDir, "../model_data/tfidfvect_new.pkl"), 'rb'))

joblib_model = pickle.load(open(os.path.join(fileDir, "../model_data/model_new.pkl"), 'rb'))


def process_text(text):
    not_punc = [char for char in text if char not in  string.punctuation]
    not_punc = "".join(not_punc)
    clean_words = [word.lower() for word in not_punc.split() if word.lower() not in stopwords.words('portuguese') ]
    return clean_words



def predict(new_text, link):    
    
    article = [new_text]
    vectorized_text = joblib_vect.transform(article)
    ynew = vectorized_text.todense()

    prediction = joblib_model.predict(ynew)
    
    probabilidade = joblib_model.predict_proba(vectorized_text)
    probabilidade = round(probabilidade[::,1].mean()*100, 2)
    
    return { "modelo": int(prediction[0]), "proba": probabilidade, "link": link, "text": new_text }