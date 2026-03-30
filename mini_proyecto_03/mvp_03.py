# El Juego de Adivinar el Número

# Preparación del juego
import random

# Bienvenida
print("Bienvenid@ a este espacio, aquí pondras a prueba tu habilidad para adivinar mi mente")

# Paso 1: Explicar las reglas
print("Yo escogeré un numero al azar entre el 1 al 50, tu misión es adivinar cual número he escogido.")
print("¿Estás list@?")

# Paso 2: Escoger el número
numero_seleccionado = random.randint(1, 50)

# Paso 3: Iniciar el juego
while True:
	respuesta_jugador = int(input("¿Que número estoy pensado?: "))

	if respuesta_jugador == numero_seleccionado:
		print("¡Correcto! Eres un(a) dios(a), dejame alabarte por siempre.")
		break
	
	elif respuesta_jugador > numero_seleccionado:
		print("Nop, mi número es menor al que pensaste, intentalo nuevamente")
	else:
		print("¡Casi!, mi número es mayor al que pensaste, intentalo nuevamente")
		continue

# Paso 4: Cierre del juego
print("Gracias por jugar conmigo un rato, eres libre de seguir tu camino hacia el éxtio.")
print("Bye bye")