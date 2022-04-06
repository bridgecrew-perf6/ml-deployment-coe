# Deploy Machine Learning Models with FastAPI
To give you a whole picture of developing an algorithm with API:

* Train a model with your own dataset and store your final model into a file. 
* Next, create a local webpage with the developed model file integrated in that page. Type any value to fit properly into the model, for example, if you developed a text classification model, you should type in text. 
* Then the webpage(integrated with model) will return the preprocessed value result for you. If you developed a score rating model, you should type in the necessary feature value regarding to the model. Then the webpage will return the score rating result for you. 

## 1. Develop you algorithm
This it the example algorithm, you can use any algorithm you want.

    '''python
    # import necessary packages
    import pandas as pd
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

    # read datasets
    df_sample_customer = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_customer.csv',index_col=[0])
    df_sample_product = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_product.csv',index_col=[0])
    df_sample_tlog = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_tlog.csv',index_col=[0])

    # join three datasets
    df_combined = df_sample_tlog.merge(df_sample_customer, on='customer_id', how='inner').merge(df_sample_product, on='upc_no', how='inner')

    # label encoding
    le = preprocessing.LabelEncoder()
    df_combined['convenience_dim_seg'] = le.fit_transform(df_combined['convenience_dim_seg'])
    df_combined['quality_dim_seg'] = le.fit_transform(df_combined['quality_dim_seg'])
    df_combined['health_dim_seg'] = le.fit_transform(df_combined['health_dim_seg'])
    df_combined['price_dim_seg'] = le.fit_transform(df_combined['price_dim_seg'])

    # drop empty values
    df_combined.dropna(inplace=True)

    # select variables
    X = df_combined[['purchase_unit', 'sales_amt']]
    y = df_combined['purchase_price']

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    # initiate linear regression model
    regr = LinearRegression()

    # train the model
    regr.fit(X_train, y_train)
    print(regr.score(X_test, y_test))

    # saving the pipeline and dump the model in your local machine
    from joblib import dump
    dump(regr, 'regression_model.joblib')
    '''
**NOTE**: you need to store this code into py file instead of ipynb. We need to execute it using terminal and generating a model file afterwards.

## 2. Install necessary packages and execute the py file 
In your terminal, install fastapi packages. 'fastapi' is the package to build webpage API. Run the following command in your terminal:

    pip install fastapi

execute your model.py file first to create a pickle model file. 
    
    py model.py

There should be one pkl file appears in your root folder. This is the backbone model that we use in the API.

Next we need to build another py file. This is the execution file that API use. I attached my code for your reference:

    # import necessary libraries
    import pandas as pd
    import joblib
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from fastapi import FastAPI

    # initializing a FastAPI App instance
    app = FastAPI()

    # load our pre-trained model
    model = joblib.load('regression_model.joblib')

    # define a function that make the predictions
    def predict_score(model, input_unit, input_amt):

        score = model.predict([[input_unit, input_amt]])[0]

        return score

    # Now that we have a FastAPI app object, we can use it to define the output for a simple get request as demonstrated below.
    @app.get('/')
    def get_root():
        return {'message': 'Welcome to the grocery recommendation API'}

    @app.get('/grocery_recommendation_query/')
    async def predict_score(input_unit, input_amt):

        score = model.predict([[input_unit, input_amt]])[0]

        return score

**NOTE:** You need to develop your own funtions to preprocess your input and make predictions afterward. This [website](https://fastapi.tiangolo.com/tutorial/first-steps/) include the reference to develop the FastAPI.

## 3. Run the command to execute the main code
    uvicorn main:app --reload
The command starts a local Uvicorn server and you should see an output similar to the output shown in the screenshot below:

![uvicorn command](https://miro.medium.com/max/997/1*YZVY4zhGEQb4WlYp9XgMKA.png)

Next, open a browser and simply type in the localhost URL: http://127.0.0.1:8000

You should see the JSON message that you created in your main file and the output as demonstrated below: 
    
    {"message":"Welcome to the grocery recommendation API"}

You could use query parameters in part of the URL. But this time we chose the documentation page to demonstrate more vividly. Navigate this in your URL: http://127.0.0.1:8000/docs

![interface](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/embedding_example/api_deployment/Images/interactable.png?raw=true)

After type the input number in my case, my input_unit=1, input_amt=2, the api displays the result. 

![api_result](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/embedding_example/api_deployment/Images/api_result.png?raw=true)

You can see the model result under the Code - Response Body block. This should be the same when you run the same input in your jupyter notebook. 