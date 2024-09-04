def cifrado_cesar(texto, corrimiento):
    resultado = ""

    # Recorrer cada carácter en el texto
    for caracter in texto:
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Obtener el código ASCII base según sea mayúscula o minúscula
            ascii_base = ord('A') if caracter.isupper() else ord('a')

            # Aplicar el corrimiento y ajustar dentro del rango de 26 letras del alfabeto
            nuevo_caracter = chr((ord(caracter) - ascii_base + corrimiento) % 26 + ascii_base)
            resultado += nuevo_caracter
        else:
            # Si no es una letra, dejar el carácter sin cambios
            resultado += caracter

    return resultado

# Solicitar al usuario que ingrese el texto y el corrimiento
texto = input("Ingresa el texto a cifrar: ")
corrimiento = int(input("Ingresa el corrimiento (número entero): "))

# Cifrar el texto
texto_cifrado = cifrado_cesar(texto, corrimiento)

# Mostrar el resultado cifrado
print(f"Texto cifrado: {texto_cifrado}")