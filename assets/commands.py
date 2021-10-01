import os
import webbrowser

def goBack() :
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)

def nodeCommands() :
    os.system("npm init -y")
    os.system("npm i express")
    os.system("npm i express-handlebars")
    os.system("npm i body-parser")
    os.system("npm i mongoose")

def gitCommit() :
    os.system("git init")
    os.system("git add.")
    os.system("git commit -m \" Auto Commit \" ")

def nodemonInit(name) :
    os.system("code " + name)
    os.system("clear")
    webbrowser.open('http://localhost:3000', new=2)
    os.system("nodemon " + name + "/app.js")