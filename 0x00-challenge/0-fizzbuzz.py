for num in range(1, 51):  # Boucle de 1 à 50 inclus
    if num % 3 == 0 and num % 5 == 0:  # Vérifie d'abord si divisible par 3 et 5
        print("FizzBuzz", end=' ')
    elif num % 3 == 0:  # Ensuite, vérifie si divisible par 3
        print("Fizz", end=' ')
    elif num % 5 == 0:  # Ensuite, vérifie si divisible par 5
        print("Buzz", end=' ')
    else:
        print(num, end=' ')  # Imprime le nombre s'il ne correspond à aucune des conditions ci-dessus
print()
