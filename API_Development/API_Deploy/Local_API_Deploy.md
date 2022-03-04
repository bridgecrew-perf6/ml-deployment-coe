# Deploy Machine Learning Models with FastAPI
To give you a whole picture of developing an algorithm with API, first you need to train a model with your own dataset and store your final model into a file. Then, create a local webpage with the developed model file integrated in the page. Type any value to fit properly into the model, for example, if you developed a text classification model, you should type in text. If you developed a score rating model, you should type in the necessary feature value regarding to the model. After you typed in your result, the webpage will generate the result through your model and return the result back to you on the webpage. 
## 1. Develop you algorithm
This it the example algorithm, you can use any algorithm you want.

    '''python

    # import necessary packages
    import pandas as pd
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

    # read datasets
    df_sample_customer = pd.read_csv('/content/drive/MyDrive/Datasets/Blend360/data/sample_customer.csv')
    df_sample_product = pd.read_csv('/content/drive/MyDrive/Datasets/Blend360/data/sample_product.csv')
    df_sample_tlog = pd.read_csv('/content/drive/MyDrive/Datasets/Blend360/data/sample_tlog.csv')

    # combined three datasets
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
    X = df_combined[['purchase_unit', 'sales_amt', 'disc_amt', 
                'convenience_dim_seg', 'quality_dim_seg', 'health_dim_seg', 'price_dim_seg',
                'convenience_dim_score', 'quality_dim_score', 'health_dim_score', 'price_dim_score']]
    y = df_combined['purchase_price']

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    # initiate linear regression model
    regr = LinearRegression()

    # train the model
    regr.fit(X_train, y_train)
    print(regr.score(X_test, y_test))

    # saving the pipeline
    from joblib import dump
    dump(regr, 'regression_model.joblib)
    '''
**NOTE**: you need to store this code into py file instead of ipynb. We need to execute it using terminal and generating a model file afterwards.

## 2. Install necessary packages and execute the py file 
In your terminal, install joblib, fastapi packages. Run the following command in your terminal:

    pip install joblib, fastapi

execute your model.py file first to create a joblib model file. 