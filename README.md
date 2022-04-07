# [Machine Learning Deployment CoE](https://ml-deployment-coe.readthedocs.io/en/latest/index.html)

## Table of Contents

- [What is it](#what-is-it)
- [How to use it](#how-to-use-it)
- [Resources](#resources)

## What is it

1. Deploy ML Models

   * Building and automating ML pipelines
     * MLOps
     * Airflow DAG
     * Cloud Services(AWS/GCP/Azure)
     * AutoML on the Cloud
   * Dynamic deploying models
     * Streamlit
     * RESTAPI
     * Docker
     * Web Services
     * Architecture

   2. Iterate, Monitor, Optimize, and Maintain the model performance
      * Revalidate Model Accuracy
      * Bayesian A/B test
      * Model Decay Detection
      * Clickstream Data
      * Digital Measurement
      * Sensitivity Analysis
      * Adversarial Attacks
      * Residual Analysis
      * Model Remediation
      * Model Fairness

## How to use it?

  You can follow the example project that we created under the projects/ folder to deploy your model to the cloud. 

### Step 1: Build Model
  In our example, we developed a recommendation algorithm using tensorflow saved in the algorithm/ folder. 
  - The data that we used are customer transaction data saved in data/ folder. 
    - There are 2938 products and 1243 customers in the dataset. 
  - We developed the algorithm using the outcome 1 or 0 based on past if customer has made a purchase or not. 
  - 
  After we created the model, we pickled the embeddings learned in the process and saved it in the model/ folder. 
  Next we created a main.py file that contains the API to be used later. 
  We can test the APIs locally by following the steps in step 2. 
### Step 2: Deploy local API

### Step 3: Deploy algorithm to Docker

### Step 4: Deploy Docker to Cloud


## Resources

