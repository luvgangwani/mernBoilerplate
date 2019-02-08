import os, subprocess, json
from pprint import pprint

textColor = "\033[1;32;40m"

def installDependencies(projectPath):

    devDependencies = ["axios", "body-parser", "bootstrap", "ejs", "express", "jquery", "mongodb", "node-sass", "node-sass-middleware", "popper.js", "prop-types", "react", "react-dom"] # list of dependencies for the development environment

    projectDependencies = ["@babel/cli", "@babel/core", "@babel/node", "@babel/preset-env", "@babel/preset-react", "babel-eslint", "babel-loader", 'eslint', "eslint-plugin-react", "nodemon", "webpack", "webpack-cli", "uglifyjs-webpack-plugin"]  # dependencies global to the project

    # install dev dependencies

    os.chdir(projectPath) # cd to projectPath

    npmDevCommand = "npm install --save-dev "
    npmProjCommand = "npm install --save "

    for devDependency in devDependencies:
        out = subprocess.Popen(npmDevCommand + devDependency, stderr=subprocess.STDOUT, shell=True)
        response, error = out.communicate()
        if error is None:
            print(textColor, devDependency, "installed! \n")
    
    for projDependency in projectDependencies:
        out = subprocess.Popen(npmProjCommand + projDependency, stderr=subprocess.STDOUT, shell=True)
        response, error = out.communicate()
        if error is None:
            print(textColor, projDependency, "installed! \n")


def addScriptsToPackageJson(projectPath):

    os.chdir(projectPath)

    with open("package.json", "r") as f:
        data = json.load(f)

    data["scripts"] = {} # empty scripts - initializing data["scripts"] to an empty dictionary to add scripts

    data["scripts"]["start"] = "nodemon --exec babel-node server.js --ignore public"
    data["scripts"]["dev"] = "webpack -wd"
    data["scripts"]["sass"] = "node-sass -w sass/ -o public/css"

    with open("package.json", "w") as f:
        json.dump(data, f, indent=4)