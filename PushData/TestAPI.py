import requests

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.json())

joke = requests.get("https://sv443.net/jokeapi/v2/joke/Programming")
print(joke.json())