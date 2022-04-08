# [Machine Learning Deployment CoE](https://ml-deployment-coe.readthedocs.io/en/latest/index.html)

## Table of Contents

- [What is it](#what-is-it)
- [How to use it](#how-to-use-it)
- [Resources](#resources)

## What is it
This is the github repository where we develop examples to deploy different types of machine learning models to cloud. 

## How to use it?

  You can use an example project that we created under [projects/](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/) and follow the steps that we described below to deploy your model. 

### Step 1: Build Model
  - In the first example project, we developed a recommender system to suggest products to customers. 
  
  ![Algorithm folder](https://github.com/yuelong12/ml-deployment-coe/blob/development/tutorials/images/algorithm_folder.png?raw=true)
  
  - In the end of ``model.ipynb`` (or you can use ``.py``) file, we pickled the model and saved it in the model/ folder:
  
  ```python
  from datetime import datetime
  import pickle
  model_timestamp = datetime.strftime(datetime.now(), "%y_%m_%d_%H_%M_%S")
  export = dict()
  export["data"] = {"product": product, "customer": customer, "sales": sales}
  export["embeddings"] = model.embeddings
  pickle.dump(export, open("../model/model_" + model_timestamp + ".pkl", "wb"))
  ```

  - Next we need to create the ``main.py`` file which contains the APIs to deploy. For example, to develop the API to recommend products to customers, we
  give a name to the API (``recommend_products``) and write a function (``customer_recommendation``) that will return the output for that call. 

  ```python
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
  ``` 
  - Save a copy of `main.py` and `model.pkl` in ``docker/app/`` folder to be used later in Step 3.  
  - Next we can test the APIs locally by following the steps in Step 2. 

### Step 2: [Test local API](https://github.com/yuelong12/ml-deployment-coe/blob/development/tutorials/test_api.md)

- Go to ``docker/app/`` where we save both the pickled model and the APIs in `main.py`, [launch](https://github.com/yuelong12/ml-deployment-coe/blob/development/tutorials/test_api.md) a local Uviron server after installing fastapi. 

- Go to http://127.0.0.1:8000/docs to see all the APIs available. 

- Test your APIs by following the detailed steps in the [link](https://github.com/yuelong12/ml-deployment-coe/blob/development/tutorials/test_api.md). 

### Step 3: [Deploy algorithm to Docker](https://github.com/yuelong12/ml-deployment-coe/blob/development/tutorials/docker_deploy.md)
- Download the Docker process directory.

- Make sure your FASTAPI is working locally by following **Step 2** above.

- Install docker desktop and keep the app open during the entire process.

- You have Dockerfile inside the `docker/` folder. It helps to:
  - Pulls the FastAPI docker image.
  - Copies the contents of the app directory to the image.
  - Makes the app directory the working directory.
  - Installs necessary dependencies.

- Go to the `docker/` folder and type this command: `docker build -t myimage .`

- Type this command: `docker run -d --name mycontainer -p 80:80 myimage`

- Now open the Docker desktop app and open the `Containers/Apps` tab, hover over the mycontainer 
and click on `Open in new browser` tab.  

### Step 4: Deploy Docker to Cloud


## Resources

