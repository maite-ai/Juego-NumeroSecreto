import random

def guess_number(secret_number, guess):
    '''Función que compara el número sugerido por el usuario y el escogido por la máquina'''
    while guess != secret_number:
        if guess > 100:
            print("¡Error! Número fuera de rango")
        elif guess > secret_number:
            print(f"El número secreto es menor que {guess}")
        else:
            print(f"El número secreto es mayor que {guess}")
        guess = int(input("\nElige otro número: "))
    return f"¡Felicidades! ¡Adivinaste! El número secreto es {secret_number}"

if __name__ == "__main__":
	# Con la función choice del módulo random, asigno un valor aleatorio a la variable «secret_number»
	secret_number = random.choice(range(1, 101))
	guess = int(input("Ingresa un número entre 1 y 100: "))
	print(guess_number(secret_number, guess))
