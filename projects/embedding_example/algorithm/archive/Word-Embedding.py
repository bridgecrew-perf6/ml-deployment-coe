#!/usr/bin/env python
# coding: utf-8

# ### Importing required libraries and reading the file

# In[52]:


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


# In[53]:

df = pd.read_csv("./test.csv")


df["upc_desc"] = df["upc_desc"].apply(lambda x: x.strip(']['))


# ## Dividing the data into train and validation datasets

customers = df["customer_id"].unique().tolist()
random.shuffle(customers)

# extract 90% of customer ID's
customers_train = [customers[i] for i in range(round(0.9*len(customers)))]

# split data into train and validation set
train_df = df[df['customer_id'].isin(customers_train)]
validation_df = df[~df['customer_id'].isin(customers_train)]


# list to capture purchase history of the customers
purchases_train = []

# populate the list with the product codes
for i in tqdm(customers_train):
    temp = train_df[train_df["customer_id"] == i]["upc_desc"].tolist()
    purchases_train.append(temp)

# list to capture purchase history of the customers
purchases_val = []

# populate the list with the product codes
for i in tqdm(validation_df['customer_id'].unique()):
    temp = validation_df[validation_df["customer_id"] == i]["upc_desc"].tolist()
    purchases_val.append(temp)


# train word2vec model
model = Word2Vec(window = 10, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)

model.build_vocab(purchases_train, progress_per=200)

model.train(purchases_train, total_examples = model.corpus_count,
            epochs=10, report_delay=1)


##Make the model more memory efficient
model.init_sims(replace=True)

from joblib import dump
dump(model, 'word2Vec.joblib')


def test_model(customer_id=190462787,topn=3):
    words = list(model.wv.index_to_key)
    df_cust = df[df["customer_id"]==customer_id] ## for multiple customer , using .isin()
    df_cust_prod = df_cust.groupby('customer_id')["upc_desc"].apply(list)
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




