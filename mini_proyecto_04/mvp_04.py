# Contador de Palabras y Caracteres

# Bienvenida
print("Bienvenid@ al contador de palabras, a continuación harémos un contéo de tu texto.")

# Paso 1: Solicitar texto al usuario
texto_usuario = str(input("Ingresa el texto que desees contar: "))

# Paso 2: Contar palabras
texto_palabras = texto_usuario.split()
resultado_palabras = len(texto_palabras)

# Paso 3: Contar Caracteres, espacio inclusive
texto_caracteres_con_espacios = (len(texto_usuario))

# Paso 4: Contar Caracteres sin el espacio
texto_caracteres_sin_espacios = texto_usuario.replace(" ", "")
resultado_caracteres = len(texto_caracteres_sin_espacios)

# Paso 5: Indicar resultados al usuario
print(f"Tu texto contiene {resultado_palabras} palabras, {texto_caracteres_con_espacios} caracteres contando espacios y {resultado_caracteres} caracteres sin contar espacios.")