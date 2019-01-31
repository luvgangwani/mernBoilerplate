import os

def addInitialFiles(projectPath, apiPath, publicPath, sassPath, srcPath):

    # Change to project path
    os.chdir(projectPath)

    listOfFiles = [
        # files at the root level
        "server.js",
        apiPath+"/index.js",
        srcPath+"/index.js",
        srcPath+"/api.js",
        sassPath+"/styles.scss"
    ]

    for eachFile in listOfFiles:
        f=open(eachFile, "w+")
        f.close()