import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Pedir al usuario que adivine
print("Adivina el número entre 1 y 100")

# Bucle que se repetirá hasta que el usuario adivine el número
intento = 0  # Inicializar el intento

while intento != numero_secreto:
    # Leer el intento del usuario y convertirlo a número entero
    intento = int(input("Escribe un número: "))
    
    # Dar pistas al usuario
    if intento < numero_secreto:
        print("El número es mayor")
    elif intento > numero_secreto:
        print("El número es menor")
    else:
        print("¡Adivinaste!")

