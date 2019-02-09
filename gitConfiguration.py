import os, subprocess

def configureGitRepo(projectPath):

    os.chdir(projectPath)

    with open(".gitignore", "w+") as f:
        f.write("node_modules/")

    gitInit = "git init"

    out = subprocess.Popen(gitInit, stderr=subprocess.STDOUT, shell=True)

    response, error = out.communicate()

    if error is None:
        return True