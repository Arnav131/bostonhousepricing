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
