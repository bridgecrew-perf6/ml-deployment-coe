import pandas as pd
import joblib
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI

# initializing a FastAPI App instance
app = FastAPI()

# load pre-trained model
model = joblib.load('regression_model.joblib')

def predict_score(model, input_unit, input_amt):

    score = model.predict([[input_unit, input_amt]])[0]

    return score

@app.get('/')
def get_root():
    return {'message': 'Welcome to the grocery recommendation API'}

@app.get('/grocery_recommendation_query/')
async def predict_score(input_unit, input_amt):

    score = model.predict([[input_unit, input_amt]])[0]

    return score