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
        f.close()

def writeConfigurations(projectPath, srcPath, publicJsPath):

    writeWebPackConfigurations(projectPath, publicJsPath)
    writeBabelConfigurations(projectPath)
    writeEslintConfigurations(projectPath)
    writeConfigJs(projectPath)

def writeWebPackConfigurations(projectPath, publicJsPath):

    os.chdir(projectPath)

    webpackConfig = {
        "entry": "./src/index.js"
    }

    webpackConfig["output"] = {}
    webpackConfig["output"]["path"] = publicJsPath
    webpackConfig["output"]["filename"] = "bundle.js"
    webpackConfig["module"] = {}
    webpackConfig["module"]["rules"] = []
    webpackConfig["module"]["rules"].append({})
    webpackConfig["module"]["rules"][0]["test"] = "/\.js$/" # print literal (raw) string as it is - FIX THIS
    webpackConfig["module"]["rules"][0]["loader"] = "babel-loader"

    webPackConfigJson = json.dumps(webpackConfig, indent = 4)

    printConfigurations(webPackConfigJson, "WEBPACK CONFIGURATIONS")

    with open("webpack.config.js", "a") as f:
        f.write("module.exports = " + webPackConfigJson)

def writeBabelConfigurations(projectPath):
    
    os.chdir(projectPath)

    babelConfig = {
        "presets" : []
    }

    babelConfig["presets"].append("@babel/preset-env")
    babelConfig["presets"].append("@babel/preset-react")

    babelConfigJson = json.dumps(babelConfig, indent=4)

    printConfigurations(babelConfigJson, "BABEL CONFIGURATIONS")

    with open(".babelrc", "w") as f:
        f.write(babelConfigJson)

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

    with open(".eslintrc.js", "w") as f:
        f.write("module.exports" + eslintConfigJson)

def writeConfigJs(projectPath):

    os.chdir(projectPath)

    configJs = "// Enter project configurations (port, host, database configurations) in this file \n"

    configJs += "const env = process.env \n"
    configJs += "export default { \n"
    configJs += "\t\tnodeEnv : env.NODE_ENV || \"development\", \n"
    configJs += "\t\tport : env.PORT || 3000, \n"
    configJs += "\t\thost : env.HOST || '0.0.0.0', \n }"

    with open("config.js", "w") as f:
        f.write(configJs)


def printConfigurations(configJson, msg):
    print("======================================")
    print(msg)
    print("======================================")
    print(configJson)
    print()