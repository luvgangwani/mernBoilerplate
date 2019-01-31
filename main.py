from projectInfo import getProjectInfo
from setupDirectories import setupDirectories
from initProject import createPackageJson
from projectDependencies import installDependencies, addScriptsToPackageJson
from initialFiles import addInitialFiles

textColor = "\033[1;32;40m"

def main():
    
    # Get project information

    projectPath = getProjectInfo()

    # Add the required directories (api, src, public, public/css, public/js, public/images, src/components)

    apiPath, srcPath, srcComponentsPath, sassPath, publicPath, publicCssPath, publicJsPath, publicImagesPath, viewsPath = setupDirectories(projectPath)    

    # Create package.json file

    if createPackageJson(projectPath):
        print(textColor, "Project initiated!")
        print(textColor, "Created the package.json file!")

    # Install dependencies
    # print(textColor, "Installing dependencies..")
    # installDependencies(projectPath)

    # Add scripts to package.json

    print("Adding scripts to package.json")

    addScriptsToPackageJson(projectPath)

    # Add initial files

    print(textColor, "Adding initial files..")

    addInitialFiles(projectPath, apiPath, publicPath, sassPath, srcPath)

if __name__ == "__main__":
    main()