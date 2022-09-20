#Calculer la factorielle d’un nombre entier, sans utiliser de fonction avancée
number = 3
def factorial(number, int) -> int:
    for i in range(2,number):
        number *= i
        return number
print(factorial(10))
