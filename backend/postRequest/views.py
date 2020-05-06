from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from pymongo import MongoClient
import requests
import json

# Create your views here.

def test_view(request):
    if request.method == 'GET':
        return HttpResponse("C'est une requête de type GET.")
    if request.method == 'POST':
        #data=request.content_params
        dict=request.POST
        # print(dict)
        # newDict=dict.copy()
        # print(type(newDict))
        print("\n")
        newDict={}
        for elem in dict:
            # print(elem)
            # print((dict.getlist(elem)))
            newDict[elem]=dict.getlist(elem)
        print(newDict)
        client = MongoClient(
            "mongodb+srv://dbUser2:dbUser2@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")

        db = client.wow_test
        #for elem in dict:
            #print(elem,dict[elem])
        print(newDict)
        db.icons.insert_one(newDict)
        return HttpResponse("C'est une requête de type POST")

def accueil(*args,**kwargs):
    return HttpResponse("<h1>Bienvenue sur le backend !! C'est un lieu interdit !!</h1>")

def getData(request):

    # nameBinary=request.body
    # nameString=nameBinary.decode('ascii')
    # print("nameString: "+nameString)
    corpsGET=request.GET
    # print("corpsGET: ")
    # print(corpsGET)
    nameString=corpsGET['pseudo']
    print("nom="+nameString)
    client = MongoClient(
        "mongodb+srv://dbUser2:dbUser2@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
    db = client.wow_test
    cursor = db.icons.find({"name":nameString})
    my_list = list(cursor)
    print(my_list)
    print(my_list[0])
    my_dict=my_list[0]
    my_dict.pop('_id')
    my_json = json.dumps(my_dict)
    print("my_json:")
    print(my_json)
    response = JsonResponse(my_dict)
    response["Access-Control-Allow-Origin"] = "https://damp-wave-14998.herokuapp.com"
    return response
