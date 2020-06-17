# ------ @author corentin ------ #

import random
import os
import string 
import json

#init de la liste contenant les villes
city = {}

# generation des villes une par une 
def generate_city(nb_ville_generer):

    for i in range (0,nb_ville_generer):

         city_name = generate_name(8)
         city_position = generate_position(nb_ville_generer)
         index = 'ville ' + str(i +1 ) 

         city[index] = [city_name, city_position]

    return city

#generation d'un nom de ville 
def generate_name(stringLenght):
    lettres = string.ascii_lowercase
    name = ''.join(random.choice(lettres) for i in range(stringLenght))
    return name 

#generation des position de la ville 
def generate_position(nb_ville_generer):
    start_rand = 0
    stop_rand = nb_ville_generer*4

    x = random.randrange(start_rand, stop_rand)
    y = random.randrange(start_rand, stop_rand)

    position = [x,y]
    
    return position



def createFile(filename, nb_ville_generer):   
    dump = generate_city(nb_ville_generer)
    filename_json = filename + '.json' 
    path_create = 'json_generate/'+ filename_json
    with open(path_create, 'w', encoding='utf-8') as f: 
        json.dump(dump, f, ensure_ascii=False)
        


print("---/ Bienvenue dans le générateur de ville \--- \n")
nb_ville_generer = int(input("Veuillez entrer le nombre de ville que vous voulez créer ... \n"))
filename = str(input("Veuillez entrer le nom de fichier que vous voulez créer ... \n"))
print("creation du fichier en cours . . . \n")
createFile(filename, nb_ville_generer)
print("Le fichier à bien été créer, à bientot...")