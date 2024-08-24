# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Verificar si el número ingresado es positivo
if n <= 0:
    print("El número debe ser entero positivo.")
else:
    # Inicializar variables para la secuencia y el resultado
    resultado = 0
    secuencia = ""

    # Generar la secuencia y calcular el resultado
    for i in range(1, n + 1):
        termino = "(1/" + str(i) + ")"  # Crear la fracción como cadena
        
        if i % 2 == 1:  # Si el índice es impar, se suma
            if i == 1:
                secuencia += termino  # Agregar el primer término sin signo
                resultado += 1 / i
            else:
                secuencia += " + " + termino  # Agregar el término con signo +
                resultado += 1 / i
        else:           # Si el índice es par, se resta
            secuencia += " - " + termino  # Agregar el término con signo -
            resultado -= 1 / i

    # Mostrar la secuencia y el resultado
    print("La secuencia es: " + secuencia)
    print("El resultado de la operación es: " + str(resultado))
