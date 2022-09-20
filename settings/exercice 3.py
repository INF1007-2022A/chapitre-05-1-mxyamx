#Calculer la somme des 100 premiers nombres entiers premiers excluant le nombre 1
count = 0
somme = 0
nombre = 2
while count < 4:

 for i in range(2,nombre):
    if nombre % i == 0:
        break
 else:
    count += 1
    somme += nombre

 nombre += 1
print(somme)