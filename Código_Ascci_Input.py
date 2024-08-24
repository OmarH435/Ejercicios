def mostrar_menu():
    print("\nMenú:")
    print("1. Convertir carácter a código ASCII")
    print("2. Convertir código ASCII a carácter")
    print("3. Salir")

def convertir_caracter_a_ascii():
    caracter = input("Ingresa un carácter: ")
    codigo_ascii = ord(caracter)
    print(f"El código ASCII de '{caracter}' es {codigo_ascii}")

def convertir_ascii_a_caracter():
    codigo_ascii = int(input("Ingresa el código ASCII: "))
    caracter = chr(codigo_ascii)
    print(f"El carácter correspondiente al código ASCII {codigo_ascii} es '{caracter}'")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            convertir_caracter_a_ascii()
        elif opcion == "2":
            convertir_ascii_a_caracter()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción válida.")

# Ejecutar el programa
main()
