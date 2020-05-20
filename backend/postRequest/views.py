from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from pymongo import MongoClient
import requests
import bcrypt
import json

# Create your views here.

def pushData(request):

    if request.method == 'GET':
        dict=request.GET
        newDict={}
        for elem in dict: # copie du dictionnaire reçue car non mutable
            newDict[elem]=dict.getlist(elem)
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post('https://us.battle.net/oauth/token', data=data,
                                 auth=('4e66ef876fe64f95955e1123a9a03bb7', 'YrEHs7S12Ufyn5mcnsAkYOVqIhtpYvx2'))
        reponseJSON = response.json()
        access_token = reponseJSON['access_token']

        currently_equipped = newDict['currently_equipped']
        url_list = []
        for elem in currently_equipped:
            if (elem == '-1'):
                url = "Defaut"
                url_list.append(url)
            else:
                r = requests.get(
                    "https://us.api.blizzard.com/data/wow/media/item/" + elem + "?namespace=static-classic-us&locale=en_US&access_token=" + access_token)
                apiResponse = r.json()
                url = apiResponse['assets'][0]['value']
                url_list.append(url)
        newDict['url_list'] = url_list

        client = MongoClient(
            "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
        db = client.wow_db

        userName = newDict['userName'][0]
        password = newDict['password'][0]

        print(userName)
        print(password)

        cursorPassword = db.account.find({"userName": userName})
        authInfo = list(cursorPassword)
        if not authInfo:
            print("Compte introuvable.")
            return HttpResponse("compte introuvable")
        dictCursor = authInfo[0]
        print(dictCursor)
        passwd1 = dictCursor['hashedPassword']

        password = password.encode(encoding='UTF-8', errors='strict')

        if bcrypt.checkpw(password, passwd1):
            print("match")
            db.data_player.delete_one({"name": newDict['name'],"userName":newDict['userName']})  # suppression des données précèdentes
            db.data_player.insert_one(newDict)  # insertion du dictionnaire dans la DB
        else:
            print("does not match")
            db.data_player.insert_one(newDict)  # insertion du dictionnaire dans la DB

        return HttpResponse("C'est une requête de type GET")

def accueil(*args,**kwargs):
    return HttpResponse("<h1>Bienvenue sur le backend !! C'est un lieu interdit !!</h1>")

def getData(request):

    corpsGET=request.GET

    nameString=corpsGET['pseudo']
    faction=corpsGET['faction']
    race=corpsGET['race']
    userName=corpsGET['user']

    client = MongoClient(
        "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
    db = client.wow_db
    cursor = db.data_player.find({"name":nameString,"raceID":race,"localizedFaction":faction,"userName":userName})
    my_list = list(cursor)


    if not my_list: #si la liste est vide cad le pseudo n'est pas trouvé dans la DB
        print("liste vide")
        response=JsonResponse({'name':'introuvable'})
    else:
        my_dict = my_list[0]
        my_dict.pop('_id')
        my_dict.pop('password') # on n'envoie pas le mot de passe sur le front-end

        #print(my_dict)

        response = JsonResponse(my_dict) #renvoie le dictionnaire en JSON
    response["Access-Control-Allow-Origin"] = "https://wow-armory-tc.herokuapp.com" #règle le problème de CORS
    return response


def loginUser(request):

    authInfo = request.GET
    userName = authInfo['pseudoInput']
    password = authInfo['passwordInput']

    print(userName)
    print(password)

    client = MongoClient(
        "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
    db = client.wow_db

    cursorPassword = db.account.find({"userName": userName})
    authInfo = list(cursorPassword)
    if not authInfo:
        response = JsonResponse({'login' : 'succes'})
        password = password.encode(encoding='UTF-8', errors='strict')
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        db.account.insert_one({'userName':userName,'hashedPassword':hashedPassword})

    else:
        response = JsonResponse({'login': 'echec'})

    response["Access-Control-Allow-Origin"] = "https://wow-armory-tc.herokuapp.com"
    return response

def authentification(request):

    authInfo=request.GET
    userName = authInfo['userName']
    password = authInfo['password']

    client = MongoClient(
        "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
    db = client.wow_db

    # print(userName)
    # print(password)

    cursorPassword = db.account.find({"userName": userName})
    authInfo = list(cursorPassword)
    if not authInfo:
        print("Compte introuvable .")
        return HttpResponse("Login inconnue .")

    dictCursor = authInfo[0]
    # print(dictCursor)
    passwd1 = dictCursor['hashedPassword']

    password = password.encode(encoding='UTF-8', errors='strict')

    if bcrypt.checkpw(password, passwd1):
        print("match")
        return HttpResponse("Authentification réussie .")
    else:
        print("does not match")
        return HttpResponse("Mot de passe erroné .")
