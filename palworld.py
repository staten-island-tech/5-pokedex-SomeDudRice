import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

# LANGAUGE SELECTION
# language = input("english, japanese, or chinese")
# for index, pokemon in enumerate(data):
#  print(index ,":", pokemon["name"][language])

# TYPE SELECTION
# yeah =0
# typechose= input("type?")
# capit= typechose.capitalize()
# for index, pocketmonster in enumerate(data):
#      if capit in pocketmonster["type"]:
#          yeah +=1
#          print (index + 1, ":", pocketmonster["name"]["english"], pocketmonster["type"])
# if yeah == 0:
#     print ("that type doesnt exist, please retype it")

# search= input()
# letters = list(search)
# for poke in data:
#     for letter in letters:
#       if letter == list(poke["name"]):

box = ["charmander"]
searc = ["c","h", "a", "r"]
if searc in list(box):
    print(1)
else:
    print (2)



          