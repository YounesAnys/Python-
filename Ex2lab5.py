#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 2

def statistiques(x):
    m = 0
    max = x[0]
    min = x[0]
    result = []

    for i in x:
        m = m + i
        if (max < i):
            max = i
        if min > i:
            min = i
        m = m / len(x)
        result.append(m)
        result.append(max)
        result.append(min)
        return result

ch = input("Veuillez entrer une liste des valeurs separée par virgules")
liste1 = list(eval(ch))
print(liste1)

liste2 = statistiques(liste1)

print("La moyenne est:", liste2[0])

print("Le max:", liste2[1])

print("Le min:", liste2[2])
