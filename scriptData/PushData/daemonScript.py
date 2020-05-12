import os.path, time
import requests
import ast
from tkinter.filedialog import *
import json
import time

def luaFileToPython(savedVariablesString): #conversion du string du LUA en JSON
    savedVariablesString = savedVariablesString.replace('["', '"')
    savedVariablesString = savedVariablesString.replace('"]', '"')
    savedVariablesString = savedVariablesString.replace('=', ': ')
    savedVariablesString = savedVariablesString.replace(" ", "")
    savedVariablesString = savedVariablesString.replace("\n", "")
    savedVariablesString = savedVariablesString.replace("true", "True")
    savedVariablesString = savedVariablesString.replace("false", "False")
    savedVariablesString = savedVariablesString.replace(":{", ":[")
    savedVariablesString = savedVariablesString.replace("{", "[")
    savedVariablesString = savedVariablesString.replace("}", "]")
    for i in range(0, 20):
        savedVariablesString = savedVariablesString.replace("--[" + str(i) + "]", "")
    savedVariablesString = savedVariablesString.replace(",	]", "]")
    savedVariablesString = savedVariablesString.replace(",		]", "]")
    savedVariablesString = savedVariablesString.replace("]'", "]")
    stringResult = "{" + savedVariablesString + "}"
    stringResult = stringResult.replace(",}", "}")
    return stringResult

def getSettings(text,name): #obtention du string à partir du nom de paramètre
    index=text.find(name)
    text2=text[index:]
    return(text2[text2.find('{')+1:len(text2)-4]) # permet d'enlever les accolades de début et fin


# def getSettingsValue(text,name):
#     index=text.find(name)
#     text2=text[index:]
#     print(text2[text2.find('=')+1:text2.find(',')])

if os.path.isfile("chemin.txt")==False: #teste s'il y a fichier chemin.txt si non il le crée
    testFichier=open("chemin.txt","w")
    testFichier.close()
chemin=open("chemin.txt","r+")
contenuChemin=chemin.read() #lit le chemin contenu dans chemin.txt
if not contenuChemin:
    print("Pas de chemin")
    filepath = askopenfilename(title="Fichier de données de jeu", filetypes=[('all files', '.*')]) #fenêtre graphique
                                                                                    # permettant d'indiquer le fichier du LUA
    print("Chemin bon : "+filepath)
    chemin.write(filepath) #écriture du chemin du fichier LUA dans chemin.txt
else:
    print(contenuChemin)
chemin.close()
chemin1=open("chemin.txt","r+")
path1=chemin1.read()
# absPath=os.path.abspath("chemin.txt")
# print(absPath)
# print("Last modified: %s" % time.ctime(os.path.getmtime(path1)))
# print("Created: %s" % time.ctime(os.path.getctime(path1)))


dateInit=time.ctime(os.path.getmtime(path1))
while(dateInit==time.ctime(os.path.getmtime(path1))): #boucle où l'on sort quand le fichier est modifié
    # print(path1)
    # print("0")
    time.sleep(2)
    pass
#print("modif")

text=open(path1,"r+")
stringSavedVariable=text.read() #lit le fichier de sortie du LUA
# print(stringSavedVariable)
stringIntoJson=getSettings(stringSavedVariable,"savedplayer") #récupération du string que l'on va convertir en JSON
# print(stringIntoJson)
jsonString=luaFileToPython(stringIntoJson) #obtention d'un JSON
dict=json.loads(jsonString) #création d'un dictionnaire à partir d'un string JSON

#print(dict)

URL_SITE = "https://mysterious-lake-46753.herokuapp.com/script"
r = requests.get(url = URL_SITE, params = dict) #requête vers le backend
# parseData=r.text
# print(parseData)