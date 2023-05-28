mot=str(input("saisir un mot "))
nb=0
for i in mot:
    if i in ["a", "e", "i", "o", "u", "y"] :
        nb+=1

print(nb)
