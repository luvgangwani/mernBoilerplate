import subprocess

def createPackageJson(projectPath):
    initCommand = "cd "+projectPath+" && npm init"

    out = subprocess.Popen(initCommand, stderr=subprocess.STDOUT, shell=True)

    response, error = out.communicate() # response holds any output given by the command, error holds any errors

    if(error is None):
        return True