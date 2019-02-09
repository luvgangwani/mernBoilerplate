from projectInfo import getProjectInfo
from setupDirectories import setupDirectories
from initProject import createPackageJson
from projectDependencies import installDependencies, addScriptsToPackageJson
from initialFiles import addInitialFiles, addContentToInitialFiles
from projectConfiguration import addConfigFiles, writeConfigurations
from gitConfiguration import configureGitRepo

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

    addInitialFiles(projectPath, apiPath, publicPath, sassPath, srcPath, viewsPath, srcComponentsPath)

    # Add content to initial files

    print(textColor, "Adding content to initial files..")

    addContentToInitialFiles(projectPath, viewsPath, srcPath, srcComponentsPath, sassPath)

    # Add config files

    print(textColor, "Adding configuration files..")

    addConfigFiles(projectPath)

    print(textColor, "Added configuration files!")

    # Write configurations

    print(textColor, "Writing configurations..")

    writeConfigurations(projectPath, srcPath, publicJsPath)

    print(textColor, "Projects configurations have been written!")

    # Git Configurations

    gitConfirm = input("Do you wish to track this project on git?(Y/N) ")

    configureGit = None

    while configureGit is None:
        if gitConfirm == "Y" or gitConfirm == "y":
            configureGit = True
        elif gitConfirm == "N" or gitConfirm == "n":
            configureGit = False
        else:
            configureGit = None
            print("Please enter Y for yes or N for no.")
    
    if not configureGit:
        pass
    else:
        if configureGitRepo(projectPath):
            print (".git folder has been created!")
            print("Add the necessary configurations and follow the steps given on your github repo page!\n")
        else:
            print("There was some error in creating the .git folder.\n")

    print("Project created!\n")
    print("Server is listening at port 3000!\n")
    print("Please open your browser and hit localhost:3000 !\n")
    

if __name__ == "__main__":
    main()