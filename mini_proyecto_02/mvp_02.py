# Conversor de Unidades (Fahrenheit a Celsius)

# Bienvenida
print("Bienvenid@ al conversor de temperatura")

# Paso 1: Solicitar ciudad
ciudad_usuario = str(input("Indique la ciudad en donde se encuentra: "))

# Paso 1: Solicitud de temperatuda en F°
grados_f = int(input("Indique los grados en Fahrenheit: "))

# Paso 2: Convertir F° a C°
grados_c = (grados_f - 32) / 1.8

# Paso 3: Indicar resultado
print(f"La ciudad de {ciudad_usuario} actualmente está a {grados_c}° Celsius")