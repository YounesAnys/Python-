#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 4

import math
def calculeEcartType(x):
    m = 0
    for i in x:
        m = m + i
    m = m / len(x)

    somme = 0
    for i in x:
        somme = somme + math.pow((i-m),2)
    ecartType = math.sqrt(somme / (len(x)-1))
    return ecartType



result = input("Veuillez entrer une liste")
liste1 = list(eval(result))

x = calculeEcartType(liste1)

print("ecart type:",x)
