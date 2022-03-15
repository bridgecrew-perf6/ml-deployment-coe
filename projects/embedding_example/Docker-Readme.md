***Steps for following the Docker process:***

1. Download the Docker process directory.
2. Test the app with FASTAPI locally.
a) Go to the app directory using `cd` in ***Anaconda prompt***
b) Type this command `uvicorn main:app --reload`
c) Then open the link "http:localhost:port_no./docs" in your browser
d) On the top right, click on `Try it out` and try your parameters.
3. Install docker desktop and keep the app open during the entire process:
4. You have Dockerfile inside the Docker process. It helps to:
a) Pulls the FastAPI docker image.
b) Copies the contents of the app directory to the image.
c) Makes the app directory the working directory.
d) Installs necessary dependencies such as Scikit-learn and Joblib.
5. Go to the `Docker process` folder and type this command: `docker build -t myimage .`
6. Type this command: `docker run -d --name mycontainer -p 80:80 myimage`
7. Now open the Docker desktop app and open the `Containers/Apps` tab, hover over the mycontainer 
and click on `Open in new browser` tab. 