# @author : corentin

import json
import os
import math
from pprint import pprint

#init des villes
ville = None

nom_fichier = input("Veuillez mettre le nom du fichier json a importer\n") + ".json"

#import du JSON de la ville
path_fichier = os.path.join("json_generate",nom_fichier)
with open(path_fichier, "r") as f : 
    ville = json.load(f)


#fonction d'implémentation de la matrice d'adjacence
def create_matrice(ville):

    matrice_adjacence = []

    for ville_a in ville.items():
        element_matrice = []
        
        x_a =  ville_a[1]['position'][0]
        y_a = ville_a[1]['position'][1]
        nom_ville_a = str(ville_a[1]['nom_ville'])

        for ville_b in ville.items():
           x_b = ville_b[1]['position'][0]
           y_b = ville_b[1]['position'][1]
           nom_ville_b = str(ville_b[1]['nom_ville'])

           if nom_ville_a == nom_ville_b:
               element_matrice.append(0)

           else:
               element_matrice.append(math.sqrt(math.pow(x_b - x_a, 2) + math.pow(y_b - y_a, 2)))

        matrice_adjacence.append(element_matrice)
    return matrice_adjacence


pprint(create_matrice(ville))






            
            
            
        
                    

