import os

textColor = "\033[1;32;40m"

def setupDirectories(projectPath):

    directories = []

    apiPath = projectPath+"/api"

    directories.append(apiPath)
    
    srcPath = projectPath+"/src"

    directories.append(srcPath)

    srcComponentsPath = projectPath+"/src/components"

    directories.append(srcComponentsPath)

    sassPath = projectPath+"/sass"

    directories.append(sassPath)

    publicPath = projectPath+"/public"

    directories.append(publicPath)

    publicCssPath = projectPath+"/public/css"

    directories.append(publicCssPath)

    publicJsPath = projectPath+"/public/js"

    directories.append(publicJsPath)
    
    publicImagesPath = projectPath+"/public/images"

    directories.append(publicImagesPath)

    viewsPath = projectPath+"/views"

    directories.append(viewsPath)

    for directory in directories:
        os.makedirs(directory)
        print(textColor, "Added", directory, "folder! \n")

    return apiPath, srcPath, srcComponentsPath, sassPath, publicPath, publicCssPath, publicJsPath, publicImagesPath, viewsPath