import os

def addInitialFiles(projectPath, apiPath, publicPath, sassPath, srcPath, viewsPath, srcComponentsPath):

    # Change to project path
    os.chdir(projectPath)

    listOfFiles = [
        # files at the root level
        "server.js",
        apiPath+"/index.js",
        srcPath+"/index.js",
        srcPath+"/api.js",
        srcComponentsPath+"/App.js",
        sassPath+"/styles.scss",
        viewsPath+"/header.ejs",
        viewsPath+"/footer.ejs",
        viewsPath+"/index.ejs"
    ]

    for eachFile in listOfFiles:
        f=open(eachFile, "w+")
        print("Created",eachFile)
        f.close()

def addContentToInitialFiles(projectPath, viewsPath, srcPath, srcComponentsPath, sassPath):

    addContentToServerJs(projectPath)
    addContentToViewFiles(projectPath, viewsPath)
    addContentToSrcIndexJs(projectPath, srcPath)
    addContentToSrcComponentsAppJs(projectPath, srcComponentsPath)
    addContentToSassStylesCSS(projectPath, sassPath)


def addContentToServerJs(projectPath):

    os.chdir(projectPath)

    print("Adding content to server.js..")

    serverJs = "import express from \"express\";\n"

    serverJs += "import config from \"./config\";\n"

    serverJs += "import path from \'path\';\n"

    serverJs += "import sassMiddleware from \'node-sass-middleware\';\n\n"

    serverJs += "\n"

    serverJs += "const app = express();\n\n"

    serverJs += "app.use(\"/bundle\", express.static(__dirname + \"/public\"))\n"
    serverJs += "app.use(\"/styles\", express.static(__dirname + \"/public/css\"))\n"
    serverJs += "app.use(\"/scripts\", express.static(__dirname + \"/public/js\"))\n"
    serverJs += "app.use(\"/img\",express.static(__dirname + \"/public/images\"))\n\n"

    serverJs += "app.use(\"/res-styles\", express.static(__dirname + \"/node_modules/bootstrap/dist/css\"))\n"
    serverJs += "app.use(\"/res-scripts\", express.static(__dirname + \"/node_modules/bootstrap/dist/js\"))\n"
    serverJs += "app.use(\"/jquery\", express.static(__dirname + \"/node_modules/jquery/dist\"))\n"
    serverJs += "app.use(\"/popper\", express.static(__dirname + \"/node_modules/popper.js/dist/umd\"))\n\n"

    serverJs += "app.use(sassMiddleware({\n"
    serverJs += "\tsrc: path.join(__dirname, \'sass\'),\n"
    serverJs += "\tdest: path.join(__dirname, \'public\')\n"
    serverJs += "}))\n\n"
    
    serverJs += "app.set(\"view engine\", \"ejs\")\n\n"

    serverJs += "app.get('/', (request, response) => {\n\n"

    serverJs += "\t\tresponse.render(\"index\",{\n\n"
    serverJs += "\t\ttitle : \"Home Page\",\n"
    serverJs += "\t\tcontent : \"Welcome to the MERN stack application\"\n\n" 
    serverJs += "\t});\n\n"
    
    serverJs += "});\n\n"

    serverJs += "app.listen(config.port, (request, response) => {\n\n"
    serverJs += "\t\tconsole.log(`Server listening at ${config.port}`)\n\n"
    serverJs += "});\n"

    writeToFile("server.js", serverJs)

def addContentToViewFiles(projectPath, viewsPath):

        addContentToHeaderEjs(projectPath, viewsPath)
        addContentToFooterEjs(projectPath, viewsPath)
        addContentToIndexEjs(projectPath, viewsPath)

def addContentToHeaderEjs(projectPath, viewsPath):

        os.chdir(projectPath)

        headerEjs = "<!DOCTYPE html>\n"
        headerEjs += "<html lang=\"en\">\n"
        headerEjs += "\t<head>\n"
        headerEjs += "\t\t<meta charset=\"UTF-8\">\n"
        headerEjs += "\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        headerEjs += "\t\t<meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n"
        headerEjs += "\t\t<link rel=\"stylesheet\" href=\"../res-styles/bootstrap.min.css\" />\n"
        headerEjs += "\t\t<link rel=\"stylesheet\" href=\"../styles/styles.css\" />\n"
        headerEjs += "\t\t<title>Naming Contest - <%= title %></title>\n"
        headerEjs += "\t</head>\n\n"
        headerEjs += "\t<body>\n"
        headerEjs += "\t\t<div class=\"container\">"

        writeToFile(viewsPath+"/header.ejs", headerEjs)


def addContentToFooterEjs(projectPath, viewsPath):

        os.chdir(projectPath)
        
        footerEjs = "\t\t</div>\n"
        footerEjs += "\t\t<script src=\"../jquery/jquery.min.js\"></script>\n"
        footerEjs += "\t\t<script src=\"../popper/popper.min.js\"></script>\n"
        footerEjs += "\t\t<script src=\"../res-scripts/bootstrap.min.js\"></script>\n"
        footerEjs += "\t\t<script src=\"../scripts/bundle.min.js\"></script>\n"
        footerEjs += "\t</body>\n\n"
        footerEjs += "</html>"

        writeToFile(viewsPath+"/footer.ejs", footerEjs)

def addContentToIndexEjs(projectPath, viewsPath):

        os.chdir(projectPath)
    
        indexEjs = "<%- include('header') -%>\n"
        indexEjs += "\t\t\t<div id = \"root\"><%- content -%></div>\n"
        indexEjs += "<%- include('footer') -%>\n"

        writeToFile(viewsPath+"/index.ejs", indexEjs)


def addContentToSrcIndexJs(projectPath, srcPath):

        os.chdir(projectPath)

        srcIndexJs = "import React from 'react';\n"
        srcIndexJs += "import ReactDOM from 'react-dom';\n"
        srcIndexJs += "import App from './components/App';\n\n"

        srcIndexJs += "ReactDOM.render(\n"
        srcIndexJs += "\t<App initialData = \"Welcome to your MERN boilerplate application!\" />,\n"
        srcIndexJs += "\tdocument.getElementById(\"root\")\n"
        srcIndexJs += ");"

        writeToFile(srcPath+"/index.js", srcIndexJs)

def addContentToSrcComponentsAppJs(projectPath, srcComponentsPath):

        os.chdir(projectPath)

        srcComponentsAppJs = "import React, { Component } from 'react';\n\n"
        srcComponentsAppJs += "class App extends Component {\n\n"
        srcComponentsAppJs += "\tconstructor(props){\n"
        srcComponentsAppJs += "\t\tsuper(props)\n"
        srcComponentsAppJs += "\t}\n\n"
        srcComponentsAppJs += "\trender() {\n"
        srcComponentsAppJs += "\t\treturn(\n"
        srcComponentsAppJs += "\t\t\t<h1>{this.props.initialData}</h1>\n"
        srcComponentsAppJs += "\t\t)\n"
        srcComponentsAppJs += "\t}\n\n"
        srcComponentsAppJs += "}\n\n"
        srcComponentsAppJs += "export default App"


        writeToFile(srcComponentsPath+"/App.js", srcComponentsAppJs)

def addContentToSassStylesCSS(projectPath, sassPath):

        os.chdir(projectPath)

        sassStylesCss = "body {\n"
        sassStylesCss += "\ttext-align: center;\n"
        sassStylesCss += "}\n"

        writeToFile(sassPath+"/styles.scss", sassStylesCss)

def writeToFile(fileName, content):
    with open(fileName, "w") as f:
        f.write(content)