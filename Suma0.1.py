# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializar la suma en 0
suma_pares = 0

# Recorrer todos los números desde 1 hasta n
for i in range(1, n + 1):
    # Verificar si el número es par
    if i % 2 == 0:
        # Sumar el número par a la suma
        suma_pares += i

# Mostrar el resultado
print(f"La suma de todos los números pares del 1 al {n} es: {suma_pares}")
