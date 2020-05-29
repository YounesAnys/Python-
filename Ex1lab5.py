#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 1 lab 5

def calculMoyenne(x):
    m = 0
    for i in x:
        m = m + i
    return m / len(x)


ch = input("Veuillez entrer une liste separée par virgules:")
liste1 = list(eval(ch))
print(liste1)

print("la moyenne est:", calculMoyenne(liste1))
