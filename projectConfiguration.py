import os, json

def addConfigFiles(projectPath):

    # add config files

    # change directory to project path

    os.chdir(projectPath)

    # list of config files

    configFiles = [
        
        "webpack.config.js",
        ".babelrc",
        ".eslintrc.js",
        "config.js"

    ]

    for eachFile in configFiles:
        f = open(eachFile, "w+")
        print("Created",eachFile + "!")
        f.close()

def writeConfigurations(projectPath, srcPath, publicJsPath):

    writeWebPackConfigurations(projectPath, publicJsPath)
    writeBabelConfigurations(projectPath)
    writeEslintConfigurations(projectPath)
    writeConfigJs(projectPath)

def writeWebPackConfigurations(projectPath, publicJsPath):

    os.chdir(projectPath)

    # webpackConfig = {
    #     "entry": "./src/index.js"
    # }

    # webpackConfig["output"] = {}
    # webpackConfig["output"]["path"] = os.getcwd() + "/public/js"
    # webpackConfig["output"]["filename"] = "bundle.js"
    # webpackConfig["module"] = {}
    # webpackConfig["module"]["rules"] = []
    # webpackConfig["module"]["rules"].append({})
    # webpackConfig["module"]["rules"][0]["test"] = "/\.js$/" # print literal (raw) string as it is - FIX THIS
    # webpackConfig["module"]["rules"][0]["loader"] = "babel-loader"

    # webPackConfigJson = "module.exports = "
    # webPackConfigJson += json.dumps(webpackConfig, indent = 4)

    # webPackConfigJson.replace("/\\\\.js$","/\\.js$")

    webPackConfigJson = "var UglifyJsPlugin = require('uglifyjs-webpack-plugin') // create minfied bundle file\n\n"
    webPackConfigJson += "module.exports = {\n"
    webPackConfigJson += "\t\"entry\": \"./src/index.js\",\n"
    webPackConfigJson += "\t\"output\": {\n"
    webPackConfigJson += "\t\t\"path\": __dirname + \"/public/js/\",\n"
    webPackConfigJson += "\t\t\"filename\": \"bundle.min.js\"\n"
    webPackConfigJson += "\t},\n"
    webPackConfigJson += "\t\"module\" : {\n"
    webPackConfigJson += "\t\t\"rules\": [\n"
    webPackConfigJson += "\t\t\t{\n"
    webPackConfigJson += "\t\t\t\t\"test\": /\.js$/,\n"
    webPackConfigJson += "\t\t\t\t\"loader\": \"babel-loader\",\n"
    webPackConfigJson += "\t\t\t},\n"
    webPackConfigJson += "\t\t],\n"
    webPackConfigJson += "\t},\n"
    webPackConfigJson += "\t\"optimization\": {\n"
    webPackConfigJson += "\t\t\"minimize\": true,\n"
    webPackConfigJson += "\t\t\"minimizer\": [\n"
    webPackConfigJson += "\t\t\tnew UglifyJsPlugin({\n"
    webPackConfigJson += "\t\t\t\t\"include\": /\.min\.js$/\n"
    webPackConfigJson += "\t\t\t})\n"
    webPackConfigJson += "\t\t]\n"
    webPackConfigJson += "\t}\n"
    webPackConfigJson += "}\n"

    printConfigurations(webPackConfigJson, "WEBPACK CONFIGURATIONS")

    writeToFile("webpack.config.js", webPackConfigJson)

def writeBabelConfigurations(projectPath):
    
    os.chdir(projectPath)

    babelConfig = {
        "presets" : []
    }

    babelConfig["presets"].append("@babel/preset-env")
    babelConfig["presets"].append("@babel/preset-react")

    babelConfigJson = json.dumps(babelConfig, indent=4)

    printConfigurations(babelConfigJson, "BABEL CONFIGURATIONS")

    writeToFile(".babelrc", babelConfigJson)

def writeEslintConfigurations(projectPath):

    os.chdir(projectPath)

    eslintConfig = {
        "parser" : "babel-eslint"
    }

    eslintConfig["env"] = {
        "browser" : "true"
    }

    eslintConfig["env"]["es6"] = "true"
    eslintConfig["env"]["commonjs"] = "true"
    eslintConfig["env"]["node"] = "true"

    eslintConfig["parserOptions"] = {
        "ecmaFeatures": {
            "jsx" : "true"
        }
    }

    eslintConfig["plugins"] = ["react"]

    eslintConfigJson = json.dumps(eslintConfig, indent=4)

    printConfigurations(eslintConfigJson, "ESLINT CONFIGURATIONS")

    writeToFile(".eslintrc.js", eslintConfigJson)

def writeConfigJs(projectPath):

    os.chdir(projectPath)

    configJs = "// Enter project configurations (port, host, database configurations) in this file \n"

    configJs += "const env = process.env \n\n"
    configJs += "export default { \n"
    configJs += "\tnodeEnv : env.NODE_ENV || \"development\", \n"
    configJs += "\tport : env.PORT || 3000, \n"
    configJs += "\thost : env.HOST || '0.0.0.0', \n}"

    writeToFile("config.js", configJs)


def printConfigurations(configJson, msg):
    print("======================================")
    print(msg)
    print("======================================")
    print(configJson)
    print()

def writeToFile(fileName, content):
    with open(fileName, "w") as f:
        f.write(content)