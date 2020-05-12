import requests
dict={"nom":"Julien","csrfmiddlewaretoken":"csrftoken"}
head = {"csrfmiddlewaretoken":"csrftoken","Referer":"http://127.0.0.1:8000/debug/"}
URL_SITE = "http://127.0.0.1:8000/debug/"
r = requests.get(url = URL_SITE,params=dict)#requête vers le backend
print(r.status_code)