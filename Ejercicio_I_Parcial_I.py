nombre = input("Ingrese su nombre: ")
Lista_Compañeros = ["Carlos Tzunun", "Neytan Yac", "Brayan Barreno", "Melissa Tzic", "Omar Herrera", "Armando Say "]

print(f"Estimado {nombre}, a continuación, verá en pantalla un menú que le proporciona las siguientes operaciones:")
print("1. Si ingresa un número positivo, verá todos los números pares desde 1 hasta el número que ingrese.")
print("2. Si ingresa un número negativo, verá todos los números impares desde ese número hasta 0.")
print("3. Si ingresa 0, verá una lista de nombres de compañeros de clase.")
print()

# ingreso de datos
numero = int(input(f"Estimado/a {nombre}, introduce un número: "))

# Verificación
if numero > 0:
    print(f"{nombre} ha ingresado un número positivo. Imprimiendo todos los números pares desde 1 hasta {numero}:")
    for i in range(2, numero + 1, 2):
        print(i)
        
elif numero < 0:
    print(f"{nombre}, el número es negativo. Imprimiendo todos los números impares desde {numero} hasta 0:")
    for i in range(numero, 0):
        if i % 2 != 0:
            print(i)
else:
    print("El número es cero. Imprimiendo la lista de nombres de los compañeros de clase:")
   
    for compañero in Lista_Compañeros:
        print(compañero)