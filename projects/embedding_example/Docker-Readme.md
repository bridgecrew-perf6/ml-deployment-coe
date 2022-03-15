***Steps for following the Docker process:***

***Step 1:*** Download the Docker process directory.  <br /><br />
***Step 2:*** Test the app with FASTAPI locally.<br />
a) Go to the app directory using `cd` in ***Anaconda prompt*** <br />
b) Type this command `uvicorn main:app --reload` <br />
c) Then open the link "http:localhost:port_no./docs" in your browser <br />
d) On the top right, click on `Try it out` and try your parameters. <br /> <br />
***Step 3:*** Install docker desktop and keep the app open during the entire process: <br /> <br />
***Step 4:*** You have Dockerfile inside the Docker process. It helps to: <br /> 
a) Pulls the FastAPI docker image. <br />
b) Copies the contents of the app directory to the image. <br />
c) Makes the app directory the working directory. <br />
d) Installs necessary dependencies such as Scikit-learn and Joblib. <br /> <br />
***Step 5:*** Go to the `Docker process` folder and type this command: `docker build -t myimage .` <br /> <br />
***Step 6:*** Type this command: `docker run -d --name mycontainer -p 80:80 myimage` <br /> <br />
***Step 7:*** Now open the Docker desktop app and open the `Containers/Apps` tab, hover over the mycontainer 
and click on `Open in new browser` tab.  