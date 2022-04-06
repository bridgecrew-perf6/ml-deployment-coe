# Machine Learning Deployment CoE

## Background

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

## Table of Contents

- [What is it](#what-is-it)
- [Why use it](#why-use-it)
- [How to use it](#how-to-use-it)
- [Prerequisite Knowledge](#prerequisite-knowledge)
- [The Weekly Plan](#the-weekly-plan)
- [Resources](#resources)


## Why use it?



## How to use it?

### Step 1: Build Model

### Step 2: Deploy local API
[Local API Deploy](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/embedding_example/api_deployment/Local_API_Deploy.md)

### Step 3: Deploy algorithm to Docker

***Step 3a :*** Download the Docker process directory.  <br /><br />
***Step 3b:*** Make sure your FASTAPI is working locally. <br /> <br />
***Step 3c:*** Install docker desktop and keep the app open during the entire process. <br /> <br />
***Step 3d:*** You have Dockerfile inside the Docker process. It helps to: <br /> 
i) Pulls the FastAPI docker image. <br />
ii) Copies the contents of the app directory to the image. <br />
iii) Makes the app directory the working directory. <br />
iv) Installs necessary dependencies such as Scikit-learn and Joblib. <br /> <br />
***Step 3e:*** Go to the `Docker process` folder and type this command: `docker build -t myimage .` <br /> <br />
***Step 3f:*** Type this command: `docker run -d --name mycontainer -p 80:80 myimage` <br /> <br />
***Step 3g:*** Now open the Docker desktop app and open the `Containers/Apps` tab, hover over the mycontainer 
and click on `Open in new browser` tab.  

### Step 4: Deploy Docker to Cloud



## The Weekly Plan

[ML Deployment and Ops COE Weekly Plan](https://app.smartsheet.com/sheets/2Pv8prh98qrCfgMQVj6GGFFxw4qjwJv6G6QCwfF1?view=gantt)


## Resources

[ML Development and Ops CoE Website](https://ml-deployment-coe.readthedocs.io/en/latest/index.html)

