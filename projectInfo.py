import os

textColor = "\033[1;32;40m"

def getProjectInfo():

    # Enter project name

    projectName = input("Enter project name: ")
    # print(projectName)
    
    # Enter project directory
    projectDir = input("Enter project directory: (Enter . for current directory and .. to got to the parent directory): ")
    # print(projectDir)

    # Create the project folder in the directory
    while not os.path.exists(projectDir):
        print(projectDir, "does not exist!")
        projectDir = input("Enter project directory: (Enter . for current directory and .. to got to the parent directory): ")
    
    # print(projectDir+"/"+projectName)

    projectPath = projectDir+"/"+projectName

    print(textColor, "Creating project folder",projectName ,"in", projectDir,"... \n")

    os.makedirs(projectPath)

    print(textColor, "Project folder named", projectName, "created in", projectDir,"! \n")

    print(textColor, "Your project path is", projectPath, " \n")

    return projectPath
