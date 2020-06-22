# @author : corentin, antonin
import matplotlib.pyplot as plt
import json
import os
import math
import random
import networkx as nx
from pprint import pprint

ville = None

with open("json_generate\\test1000.json", "r") as f : 
    ville = json.load(f)

coor_x = []
coor_y = []

G = nx.Graph()

def create_matrice(ville):

    matrice_adjacence = []

    index = 0

    for ville_a in ville.items():
        element_matrice = []

        index = index+1
        
        x_a =  ville_a[1]['position'][0]
        coor_x.append(x_a)
        y_a = ville_a[1]['position'][1]
        coor_y.append(y_a)
        nom_ville_a = str(ville_a[1]['nom_ville'])
        G.add_node(index, pos=(x_a,y_a))

        index2 = 0
        conn = 0

        for ville_b in ville.items():

           index2 = index2+1
           x_b = ville_b[1]['position'][0]
           y_b = ville_b[1]['position'][1]
           nom_ville_b = str(ville_b[1]['nom_ville'])


           if nom_ville_a == nom_ville_b:
               element_matrice.append(0)

           else:
               distance = math.sqrt(math.pow(x_b - x_a, 2) + math.pow(y_b - y_a, 2))
               if (distance < 200):
                   G.add_edge(index, index2)
               element_matrice.append(math.sqrt(math.pow(x_b - x_a, 2) + math.pow(y_b - y_a, 2)))
        matrice_adjacence.append(element_matrice)
    return matrice_adjacence


matrice = create_matrice(ville)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,node_size=10)

plt.show()
