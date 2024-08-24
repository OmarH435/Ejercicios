# Definir el tamaño del diamante
altura = 5  # Cambia este valor para hacer el diamante más grande o más pequeño

# Parte superior del diamante
for i in range(altura):
    print(' ' * (altura - i - 1) + '*' * (2 * i + 1))

# Parte inferior del diamante
for i in range(altura - 2, -1, -1):
    print(' ' * (altura - i - 1) + '*' * (2 * i + 1))
