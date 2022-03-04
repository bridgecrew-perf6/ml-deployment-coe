import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
return {'message': 'Welcome to the grocery recommendation API'}