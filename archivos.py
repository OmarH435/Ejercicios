def leerarchivo(nombrearchivo):
    with open(nombrearchivo, "r") as archivo:
        contenido=archivo.read()
    return contenido

#funcion escribir archivo

def escribirarchivo (nombrearchivo,texto):
    with open(nombrearchivo, "a") as archivo: #a es para agregar texto al final
        archivo.write(texto)
    
nombrearchivo="miarchivo.txt" # nombre del archivo a editar

print ("estoy leyendo el acrchivo...")

contenido=leerarchivo(nombrearchivo) # es imporante que el archivo este alojado en la misma carpeta del programa
print("lo que lepi en el archivo es :")
print(contenido)

# bloque para escribir en mi archivo.
nuevaslineas= "\n Línea4: Hola, esta es una nueva línea agregada. \n Línea5: esta es otra línea agregada"
print("Estoy Agregando nuevas líneas a su archivo")
escribirarchivo(nombrearchivo,nuevaslineas)
print("He agregado líneas a su archivo")

# mostrar al usuario el contenido ya actualizado
print("\n estoy leyendo ty archivo en este momento")
print("\n el contenido de tu archivo es:")
contenidoactualizado=leerarchivo(nombrearchivo)
print(contenidoactualizado)


