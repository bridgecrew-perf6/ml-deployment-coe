import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import re
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy.spatial.distance import cdist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import normalize
from wordcloud import WordCloud
from datetime import datetime
import random
from tqdm import tqdm
from gensim.models import Word2Vec


app = FastAPI()

@app.get('/')
def get_root():
    return {'message': 'Welcome to the spam detection API'}

model = joblib.load('word2Vec.joblib')
df = pd.read_csv("./test.csv")
df["upc_desc"] = df["upc_desc"].apply(lambda x: x.strip(']['))

def test_model(customer_id : int=190462787, topn :int=3):
    print(customer_id)
    words = list(model.wv.index_to_key)
    df_cust = df[df["customer_id"] == customer_id]  ## for multiple customer , using .isin()
    df_cust_prod = df_cust.groupby('customer_id')["upc_desc"].apply(list)
    print(df_cust_prod[customer_id])
    recommended_products = []
    ## Can add another outer for loop for multiple customer recommendation
    ## Finding the intersection of above 69 vocab products and the customer's bought products
    most_common_bought_products = set(words).intersection(set(df_cust_prod[customer_id]))
    for products in most_common_bought_products:
        recommended_products.append(model.wv.most_similar(products, topn=topn))

    ## add 2 more conditions:
    ## first make recommended products unique and convert it into a set
    ## second check if recommended products already exists in df_cust_prod[customer_id])
    return recommended_products

@app.get('/')
def get_root():
    return {'message': 'Welcome to the grocery recommendation API'}

@app.get('/grocery_recommendation_query/')
async def test_model(customer_id : int =190462787, topn : int=3):
    print(customer_id)
    words = list(model.wv.index_to_key)
    df_cust = df[df["customer_id"] == customer_id]  ## for multiple customer , using .isin()
    df_cust_prod = df_cust.groupby('customer_id')["upc_desc"].apply(list)
    print(df_cust_prod[customer_id])
    recommended_products = []
    ## Can add another outer for loop for multiple customer recommendation
    ## Finding the intersection of above 69 vocab products and the customer's bought products
    most_common_bought_products = set(words).intersection(set(df_cust_prod[customer_id]))
    for products in most_common_bought_products:
        recommended_products.append(model.wv.most_similar(products, topn=topn))

    ## add 2 more conditions:
    ## first make recommended products unique and convert it into a set
    ## second check if recommended products already exists in df_cust_prod[customer_id])
    return recommended_products