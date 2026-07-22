# Convertir a mayusculas
def main():
    contador = 0
    while True:
        entrada = input("Palabra o numero (espacio termina): ")
        if entrada == " ":
            break
        try:
            if entrada.isdigit():
                entrada = str(entrada)
            print(entrada.upper())
            contador += 1
        except Exception as e:
            print("Error: ", e)

    # Estas líneas deben ir dentro de la función (con sangría)
    print("Programa terminado")
    print("Cantidad de palabras procesadas: ", contador)


# Dos líneas en blanco antes de llamar a la función
main()


# Deja una última línea completamente vacía aquí abajo al final del archivo