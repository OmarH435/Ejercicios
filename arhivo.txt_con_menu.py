# Función para leer el archivo
def leerarchivo(nombrearchivo):
    try:
        with open(nombrearchivo, "r") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no existe aún. Crea el archivo primero."

# Función para escribir en el archivo
def escribirarchivo(nombrearchivo, texto):
    with open(nombrearchivo, "a") as archivo:  # "a" agrega texto al final del archivo
        archivo.write(texto + "\n")
    print("Texto agregado al archivo.")

# Función para crear un archivo nuevo
def creararchivo(nombrearchivo):
    try:
        with open(nombrearchivo, "x") as archivo:  # "x" crea el archivo, falla si ya existe
            archivo.write("Archivo creado exitosamente.\n")
        print(f"Archivo '{nombrearchivo}' creado con éxito.")
    except FileExistsError:
        print(f"El archivo '{nombrearchivo}' ya existe.")

# Menú interactivo para el usuario
def menu():
    nombrearchivo = "miarchivo.txt"  # Nombre del archivo a leer/escribir

    while True:
        print("\n--- Menú ---")
        print("1. Crear archivo")
        print("2. Leer archivo")
        print("3. Escribir en archivo")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            creararchivo(nombrearchivo)
        elif opcion == "2":
            print("\nLeyendo archivo...")
            contenido = leerarchivo(nombrearchivo)
            print("Contenido del archivo:")
            print(contenido)
        elif opcion == "3":
            texto = input("Escribe el texto que deseas agregar al archivo: ")
            escribirarchivo(nombrearchivo, texto)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciar el programa
menu()
