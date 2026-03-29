# Calculadora de Propinas

# Bienvenida
print("Bienvenid@ a la Propinadora. A continuación calcularemos cuanta propina debe dar.")

# Paso 1: Pedir el total de la cuenta
total_cuenta = float(input("¿Cuál es el total de la cuenta? (sin puntos): "))

# Paso 2: Solicitar el procentaje de propina a dejar
porcentaje_propina = float(input("Ingrese el porcentaje de propina a dejar (sin puntos ni porcentaje): "))

# Paso 3: Confirmar cantidad de personas a colaborar
cantidad_personas = int(input("¿Cuantas personas van a aportar?: "))

# Paso 4: Realizar el calculo
total_propina = (total_cuenta * (porcentaje_propina / 100))
cuota_por_persona = (total_propina / cantidad_personas)

# Paso 5: Indicar el resultado
print(f"El total de propina a pagar es ${total_propina} YEN. Adicional cada persona debe aportar la cantidad de ${cuota_por_persona} YEN")