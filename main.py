import os
from assets.commands import *

os.system("service mongod start")

f = open("assets/nodeCode.txt", "r")
node = f.read()

f = open("assets/jsFunctions.txt", "r")
js = f.read()

f = open("assets/htmlCode.txt", "r")
html = f.read()

f = open("assets/htmlBoilerplate.txt", "r")
boiler = f.read()

f = open("assets/cssCode.txt", "r")
css = f.read()

goBack()

os.chdir("Documents/Websites")

projectName = input("Enter Your Project Name : ")
os.mkdir(projectName)
os.chdir(projectName)

os.mkdir("views")
os.chdir("views")

f = open("index.handlebars", "w")
f.write(html)
f.close()

os.mkdir("layouts")
os.chdir("layouts")

f = open("main.handlebars", "w")
f.write(boiler)
f.close()

goBack()
goBack()

os.mkdir("public")
os.chdir("public")

os.mkdir("css")
os.mkdir("images")
os.mkdir("javascript")

os.chdir("css")

f = open("styles.css", "w")
f.write(css)
f.close()

goBack()

os.chdir("javascript")

f = open("jsFunctions.js", "w")
f.write(js)
f.close()

goBack()
goBack()

f = open("app.js", "w")
f.write(node)
f.close()

runBuild()