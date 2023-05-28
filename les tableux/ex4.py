tab = []

for i in range(6):
    chaine = input("Saisissez une chaîne de caractères : ")
    tab.append(chaine)

print(max(tab,key=len))