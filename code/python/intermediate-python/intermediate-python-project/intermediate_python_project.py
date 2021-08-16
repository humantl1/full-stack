# 1. prompt for user input: which pokemon
#   [offer selection of poke, use api offset to display 20 pokes at a time]
# 2. create dynamic url based on step 1
# 3. fetch data from url made in step 2
# 4. convert json data into dictionary
# 5. print data
#   [print basic data. offer additional data via prompt]

import requests

usr_in = input("""Enter Pokemon name, numbers 1 - 1118,
or D to display pokemon""").lower()
print(f"You entered [{usr_in}]")
url = "https://pokeapi.co/api/v2/pokemon/" + usr_in
print(f"Url: {url}")

req = requests.get(url)
print(type(req))
poke = req.json()
print(f"""Name: {poke["name"]}
Base Experience: {poke["base_experience"]}
Height: {poke["height"]}
Weight: {poke["weight"]}
""", end = '')
print("Abilities:")
for ability in poke["abilities"]:
    print("  " + ability["ability"]["name"])
print("Moves:")
for move in poke["moves"]:
    print("  " + move["move"]["name"])