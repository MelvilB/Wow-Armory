from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from pymongo import MongoClient
import requests
import json

# Create your views here.

def pushData(request):
    # if request.method == 'GET':
    #     return HttpResponse("C'est une requête de type GET.")
    if request.method == 'GET':
        #data=request.content_params
        dict=request.GET
        # print(dict)
        # newDict=dict.copy()
        # print(type(newDict))
        print("\n")
        newDict={}
        for elem in dict:
            # print(elem)
            # print((dict.getlist(elem)))
            newDict[elem]=dict.getlist(elem)
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post('https://us.battle.net/oauth/token', data=data,
                                 auth=('4e66ef876fe64f95955e1123a9a03bb7', 'YrEHs7S12Ufyn5mcnsAkYOVqIhtpYvx2'))
        #print(response.json())
        reponseJSON = response.json()
        # dict=json.loads(response)
        access_token = reponseJSON['access_token']
        # print(access_token)

        currently_equipped = newDict['currently_equipped']
        #print(currently_equipped)
        url_list = []
        for elem in currently_equipped:
            if (elem == '-1'):
                #print("Pas d'objet sur l'emplacement.")
                url = "Defaut"
                url_list.append(url)
            else:
                r = requests.get(
                    "https://us.api.blizzard.com/data/wow/media/item/" + elem + "?namespace=static-classic-us&locale=en_US&access_token=" + access_token)
                # print(r.json())
                apiResponse = r.json()
                url = apiResponse['assets'][0]['value']
                #print("url: " + url)
                url_list.append(url)
        newDict['url_list'] = url_list
        #print(newDict)
        client = MongoClient(
            "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
        db = client.wow_db
        #for elem in dict:
            #print(elem,dict[elem])
        #print(newDict)
        #element=newDict['name']
        #print(element)
        db.data_player.delete_one({"name": newDict['name']}) #suppression des données précèdentes
        db.data_player.insert_one(newDict) #insertion du dictionnaire dans la DB
        return HttpResponse("C'est une requête de type GET")

def accueil(*args,**kwargs):
    return HttpResponse("<h1>Bienvenue sur le backend !! C'est un lieu interdit !!</h1>")

def getData(request):
    # data = {
    #     'grant_type': 'client_credentials'
    # }
    #
    # response = requests.post('https://us.battle.net/oauth/token', data=data,
    #                          auth=('4e66ef876fe64f95955e1123a9a03bb7', 'YrEHs7S12Ufyn5mcnsAkYOVqIhtpYvx2'))
    # print(response.json())
    # reponseJSON = response.json()
    # # dict=json.loads(response)
    # access_token = reponseJSON['access_token']
    # #print(access_token)
    # r = requests.get(
    #     "https://us.api.blizzard.com/data/wow/media/item/19019?namespace=static-classic-us&locale=en_US&access_token=" + access_token)
    # #print(r.json())
    #apiResponse=r.json()
    # nameBinary=request.body
    # nameString=nameBinary.decode('ascii')
    # print("nameString: "+nameString)
    corpsGET=request.GET
    # print("corpsGET: ")
    # print(corpsGET)
    nameString=corpsGET['pseudo']
    faction=corpsGET['faction']
    #print("faction="+faction)
    race=corpsGET['race']
    #print("race="+race)
    #print("nom="+nameString)
    client = MongoClient(
        "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
    db = client.wow_db
    cursor = db.data_player.find({"name":nameString,"raceID":race,"localizedFaction":faction})
    my_list = list(cursor)
    #print(my_list)
    # print(my_list[0])

    if not my_list: #si la liste est vide cad le pseudo n'est pas trouvé dans la DB
        print("liste vide")
        response=JsonResponse({'name':'introuvable'})
    else:
        my_dict = my_list[0]
        my_dict.pop('_id')
        #print(my_dict)
        # currently_equipped=my_dict['currently_equipped']
        # for elem in currently_equipped:
        #     r = requests.get(
        #         "https://us.api.blizzard.com/data/wow/media/item/"+elem+"?namespace=static-classic-us&locale=en_US&access_token=" + access_token)
        #     #print(r.json())
        #     apiResponse = r.json()
        #     url=apiResponse['assets'][0]['value']
        #     print("url: "+url)

        response = JsonResponse(my_dict) #renvoie le dictionnaire en JSON
    response["Access-Control-Allow-Origin"] = "https://damp-wave-14998.herokuapp.com" #règle le problème de CORS
    return response
def testCSRF(request):
    dict2 = request.GET
    print(dict2)
    return HttpResponse("Yo")