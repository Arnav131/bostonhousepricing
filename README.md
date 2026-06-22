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

  