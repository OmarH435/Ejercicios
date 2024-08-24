def convertir_a_ascii(cadena):
    valores_ascii = [ord(caracter) for caracter in cadena]
    return valores_ascii

def sumar_ascii(valores_ascii):
    return sum(valores_ascii)

def es_mayuscula(caracter):
    return 'Sí' if caracter.isupper() else 'No'

def main():
    # Solicitar una cadena de texto al usuario
    cadena = input("Ingresa una cadena de texto: ")
    
    # Convertir la cadena a valores ASCII
    valores_ascii = convertir_a_ascii(cadena)
    print(f"Valores ASCII de la cadena: {valores_ascii}")
    
    # Realizar una suma de los valores ASCII
    suma = sumar_ascii(valores_ascii)
    print(f"La suma de los valores ASCII es: {suma}")
    
    # Determinar si cada carácter es una letra mayúscula
    for caracter in cadena:
        resultado = es_mayuscula(caracter)
        print(f"¿El carácter '{caracter}' es una letra mayúscula? {resultado}")

# Ejecutar el programa
main()
