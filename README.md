# bostonhousepricing


### Boston House Pricing Prediction


### Software And Tools Requirements
1. [Github Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/downloads)
5. [Python](https://www.python.org/downloads/)

### Create a new environment 
```bash
conda create -p venv python==3.8 -y
conda activate venv/
```

### Start writing the code
requirements.txt file to install all the dependencies
```bash
pip install -r requirements.txt
```
### Setting up the GIT
* every code we write over here will be pushed to the github repository. So, we need to set up the git in our local machine.
1. setting email in gitCL: 
```bash
git config --global user.email "your_email@example.com"
```
2. setting name in gitCL: 
```bash
git config --global user.name "Your Name"
```
3. setting default branch name in gitCL: 
```bash
git config --global init.defaultBranch main
```
### Some basic git commands
1. git init: to initialize the git repository in our local machine.
```bash
git init
```
2. to add only specific files to the staging area.
```bash
git add <file_name>
```
3. git add: to add all the files to the staging area.
```bash 
git add .
```
4. To check the status of the files in the staging area.
```bash
git status
```
5. git commit: to commit the changes to the local repository.
```bash
git commit -m "commit message"
```
6. git push: to push the changes to the remote repository.
```bash
git push origin main
```

## CREATING AN app.py FILE USING FLASK WHICH IS CONFIGURED ON BEHALF OF THE MODEL TO PREDICT THE HOUSE PRICES USING THE PICKEL FILE

* once the app.py file is created we now download postman to test the api created using flask

## downloading the postman from the link below
[Postman](https://www.postman.com/downloads/)

after downloading the postman if you want to learn about how postman test the api without any actual front end then see our Learning_Notes.md
* now we test the app.py -> in terminal run the command :
```bash
python app.py
```
and in postman we test the api using the url : http://127.0.0.1:5000/predict_api
```json
{data:
    {
    "CRIM": 0.00632,
    "ZN": 18.0,
    "INDUS": 2.31,
    "CHAS": 0.0,
    "NOX": 0.538,
    "RM": 6.575,
    "AGE": 65.2,
    "DIS": 4.09,
    "RAD": 1.0,
    "TAX": 296.0,
    "PTRATIO": 15.3,
    "B": 396.9,
    "LSTAT": 4.98
    }
}
```


### NOW PUSHING THE CODE TO GITHUB REPOSITORY -> Frequently we will be pushing the code to the github repository so that we can keep track of the changes made in the code and also we can revert back to the previous version of the code if needed.





# Now since our app.py is working and tested under postman , no we will code a basic fronend using html and css.



# **WE WILL USE THREE DEPLOYEMENT METHODS**
    1. Deploying the app on heroku ### this is not free now so we will not be using this method ###
    2. Deploying using docker
    3. Deploying using Github_Actions (Github CI/CD pipeline).

## **DEPLOYING THE APP ON RENDER**
    Deploting the application on the Render
    Go to Render.com and create a free account.

1. Click the New + button in the dashboard and select Web Service.

2. Connect your GitHub account and select your repository from the list.

3. Fill out the configuration settings:

     Application Name: A unique name for your application.

     Region: Choose the region closest to you or your users.

     Branch: main (or your default branch).

     Runtime: Python

     Build Command: pip install -r requirements.txt

    Start Command: This depends on your specific Python framework (e.g., gunicorn app:app).

4. Scroll down, select the Free instance type, and click Deploy Web Service.

## **DEPLOYING THE APP USING DOCKER**
    1. Create a dockerfile in the root directory of the project.
    2. Write the following code in the dockerfile.
    ```dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.8-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install -r requirements.txt

    # Make port 5000 available to the world outside this container
    EXPOSE $PORT

    # Run app.py when the container launches
    CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app


## After Docker is created in order to use github Actions we need to create a workflow file in the {.github/workflows} directory of the project.

we will create a file named {render.yml} in the {.github/workflows} directory of the project and write the following code in it.

```yaml



### Github Actions CI/CD pipeline is used to automate the deployement to the render everytime we push the code {any changes or updates} to the github repository. <mark> if you want to learn more about how  github actions work then see our Learning_Notes.md file</mark>