print("Estimado usuario, a continuación se le solicita que pueda ingresar un carácter, para saber el código ASCII que le corresponde. En caso de no querer continuar, escriba 'Salir'.")
print("Menú")
print("Ingrese el número 1, para convertir un carácter a código ASCII")
print("Para finalizar, escriba 'Salir'") 

menu = input()

if menu == '1':
    while True:
        caracter = input("Ingrese un carácter (o 'Salir' para terminar): ")
        if caracter == 'Salir':
            break
        if len(caracter) == 1:
            valor_ascii = ord(caracter)
            print("El código ASCII del carácter", caracter, "es:", valor_ascii)
        else:
            print("Por favor, ingrese solo un carácter.")
    
print("Gracias por utilizar el programa. ¡Hasta luego!")