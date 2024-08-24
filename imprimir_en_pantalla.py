print("Por favor, ingresa tu nombre:")
nombre = input()
print("Hola, " + nombre + ". Ahora ingresa tu edad:")
edad = int(input())  # Convertimos la entrada en un número entero
mensaje = "Tienes " + str(edad) + " años. Eres "

if edad < 19:
    mensaje += "menor de edad"
else:
    mensaje +="mayor de edad"

print(mensaje)