# Deploy Machine Learning Models with FastAPI

## 0. Install fastapi
    pip install fastapi

## 1. Run the command to launch a local Uviron server
    uvicorn main:app --reload
The command starts a local Uvicorn server and you should see an output similar to the output shown in the screenshot below:

![uvicorn command](https://miro.medium.com/max/997/1*YZVY4zhGEQb4WlYp9XgMKA.png)

## 2. Open a browser and go to http://127.0.0.1:8000

You should see the JSON message that you created in your main file and the output as demonstrated below: 
    
    {"message":"Welcome to the grocery recommendation API"}

You could use query parameters in part of the URL. But this time we chose the documentation page to demonstrate more vividly. Navigate this in your URL: http://127.0.0.1:8000/docs

![interface](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/embedding_example/api_deployment/Images/interactable.png?raw=true)

## 3. Test your API functions
After type the input number in my case, my input_unit=1, input_amt=2, the api displays the result. 

![api_result](https://github.com/yuelong12/ml-deployment-coe/blob/development/projects/embedding_example/api_deployment/Images/api_result.png?raw=true)

You can see the model result under the Code - Response Body block. This should be the same when you run the same input in your jupyter notebook. 