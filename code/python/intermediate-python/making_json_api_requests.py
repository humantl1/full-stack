import requests

req = requests.get("https://swapi.dev/api/people/2/")
print(type(req))
person = req.json()
print(f"Name is\t\t\t{person['name']}")
print(f"Birth year is\t\t{person['birth_year']}")

#this is the same recursive GET requests i was making for my javascript project
print("Films involved in:")
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print(f"Film is: {film['title']}")