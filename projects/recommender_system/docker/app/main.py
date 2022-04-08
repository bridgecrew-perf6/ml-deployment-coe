import pandas as pd
import numpy as np
import pickle
from fastapi import FastAPI
import os

app = FastAPI()
model = pickle.load(open('../model/model_22_03_28_11_41_52.pkl', "rb"))
DOT = 'dot'
COSINE = 'cosine'
product = model["data"]["product"]
customer = model["data"]["customer"]
sales = model["data"]["sales"]
embeddings = model["embeddings"]

# helper function
def compute_score(query_embedding, item_embeddings, measure = COSINE):
    u = query_embedding
    V = item_embeddings
    if measure == COSINE:
        u = u / np.linalg.norm(u)
        V = V / np.linalg.norm(V, axis = 1, keepdims = True)
    return u.dot(V.T)

# api
@app.get('/')
def get_root():
    max_id = max(customer.customer_id_code.values)
    return 'Welcome to the grocery recommendation API. There are %d customers to recommend products to. Find recommendations by their id ranging from 0 to %d.' % (max_id + 1, max_id)

@app.get("/get_customer_id/")
async def get_customer_id():
    return customer.customer_id_code.values

@app.get("/get_product_id/")
async def get_product_id():
    return product.upc_no_code.values

@app.get("/customer_history/")
async def customer_history(customer_id):
    customer_id = int(customer_id)
    products_purchased = list(sales[sales.customer_id == customer_id].upc_no.unique())
    products_purchased_desc = product[product.apply(lambda x: x["upc_no_code"] in products_purchased, axis = 1)].upc_desc.unique()
    return ", ".join(products_purchased_desc)

@app.get("/recommend_products/")
async def customer_recommendation(customer_id, measure = COSINE, k = 10, exclude_bought = False):
    customer_id = int(customer_id)
    k = int(k)
    scores = compute_score(
        embeddings["customer_id"][customer_id], 
        embeddings["upc_no"], 
        measure
    )
    score_key = measure + " score"
    df = pd.DataFrame({
        score_key: list(scores),
        "product id": product["upc_no_code"],
        "product name": product["upc_desc"],
        "category": product["category_desc_level_1"],
        "subcategory": product["category_desc_level_2"]
    })
    if exclude_bought:
        bought_items = sales.query("customer_id == @customer_id")["upc_no"].unique()
        df = df[df["product id"].apply(lambda x: x not in bought_items)]
    output = ", ".join(df.sort_values([score_key], ascending = False).head(k)["product name"].values)
    return output

@app.get("/similar_products/")
async def product_neighbors(desc, measure = COSINE, k = 10):
    k = int(k)

    ids = product[product["upc_desc"].str.contains(desc.upper())].index.values
    descs = product.iloc[ids]["upc_desc"].values
    
    if len(descs) == 0:
        raise ValueError("Found no products for %s" % desc)
    print("Nearest neighbors of : %s." % descs[0])
    
    if len(descs) > 1:
        print("Found more than 1 matching product. Other candidates: {}".format(", ".join(descs[1:])))

    prod_id = ids[0]
    scores = compute_score(
        embeddings["upc_no"][prod_id], embeddings["upc_no"], measure
    )
    score_key = measure + " score"
    df = pd.DataFrame({
        score_key : list(scores),
        "product name": product["upc_desc"],
        "category": product["category_desc_level_1"],
        "subcategory": product["category_desc_level_2"]
    })
    output = ", ".join(df.sort_values([score_key], ascending = False).head(k)["product name"].values)
    return output