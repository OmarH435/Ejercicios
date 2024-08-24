# Solicitar al usuario un número entero
n = int(input("Introduce un número para mostrar su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar desde 1 hasta 10
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    # Calcular y mostrar el resultado de la multiplicación
    print(f"{n} x {i} = {n * i}")
