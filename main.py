import random
from validation import Validation

# Con la función choice del módulo random, asigno un valor aleatorio a la variable «secret_number»
secret_number = random.choice(range(1, 101))
number = int(input("Ingresa un número entre 1 y 100: "))

if Validation.is_number(number):
    # El código itera las veces que sean necesarias hasta que adivine el número secreto.
	while number != secret_number:
		if number > 100:
			print("¡Error! Número fuera de rango")
		elif number > secret_number:
			print(f"El número secreto es menor que {number}")
		else:
			print(f"El número secreto es mayor que {number}")
		number = int(input("\nElige otro número: "))
else:
    raise TypeError("Tienes que ingresar un valor numérico  ")
	

print(f"¡Felicidades! ¡Adivinaste! El número secreto es {secret_number}")