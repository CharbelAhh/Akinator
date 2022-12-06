from pandas import *

f=read_csv("data.csv")

table=[[reponse for reponse in f]] # liste/matrice avec tout les valeurs du tableau

for i in f:
    col=[]
    for j in f[i]:
        col.append(j)
    table.append(col) # boucle pour remplir la liste

valide=table[1] # liste contenant les noms valide

for Question in table[0]:
    if Question!="Nom":
        while True:
            choix=input(Question+" (O/N)\n").lower()
            reponses=table[table[0].index(Question)+1] # reponses de la question
            
            if choix in ["o","oui"]:
                for i in range(len(reponses)-1,-1,-1):
                    if not reponses[i]:
                        valide[i]=""
                break
            elif choix in ["n","non"]:
                for i in range(len(reponses)-1,-1,-1):
                    if reponses[i]:
                        valide[i]=""
                break
            else:
                print("Pas un choix.")
    
    noms=[nom for nom in valide if nom]
    if len(noms)==1:
        print("Votre character est "+noms[0])
        break
    elif not(len(valide)):
        print("Vous avez gagner! je n'ai pas pu trouver votre charactere.")
        break
else:
    print("Vous avez gagner! je n'ai pas pu trouver votre charactere.")