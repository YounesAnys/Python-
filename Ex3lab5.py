#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 3

import math

def calculeDistances(vitesse):
    dist = []
    g = 9.8
    deg_a_rad = math.pi / 180.0

    nombre_dangles = 10

    theta = 0

    while theta < 90:
        thetaRad = deg_a_rad * theta
        dist.append(2.0 * vitesse * vitesse * math.cos(thetaRad) * (math.sin(thetaRad) / g))
        theta = theta + 10
    return dist
vitesse = float(input("S.V.P donnez la vitesse en m/s"))
distances = calculeDistances(vitesse)
index = 0
while index < len(distances):
    theta = index * 10
    print("pour l'angle",theta,"degrees, la balle parcours",distances[index],"metres")
    index = index + 1
