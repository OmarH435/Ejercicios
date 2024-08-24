print("Estimado usuario, a continuación se le solicita que pueda ingresar un número que se considerara como final, y se realizará la suma de los numeros pares anteriores")
print("Ingrese un número")
suma_pares = int(input())
for i in range(1, int(suma_pares+1)):
    if i % 2 == 0:
        print(i)
        suma_pares += i
print("La suma de los números pares es:", int(suma_pares))