import random

def jugar_adivinar_numero():
    #1 la configuracion inicial
    print("Hola, vamos a jugar!")
    print("Piensa en un numero random, adivina cual es")

    #la pc elige numero random
    numero_oculto = random.randint(1,99)
    intentos = 0
    adivinado = False

    #2 aca va el bucle para la adivinanza
    while not adivinado:
        eleccion_usuario = input("Ingresa un numero: ")
        if not eleccion_usuario.isdigit():
            print("Ingresa un numero entero: ")
            continue #esto vuelve al inicio del bucle

        eleccion_usuario = int(eleccion_usuario)
        intentos += 1 #para sumar +1 a los intentos

        #aca lo logico para adivinar
        if eleccion_usuario < numero_oculto:
            print("Muy bajo, Intenta de nuevo")
        elif eleccion_usuario > numero_oculto:
            print("Muy alto, Intenta de nuevo")
        else:
            adivinado = True
            print(f"Adivinaste! el {numero_oculto} en {intentos} intentos")

#ejecutar y probar

jugar_adivinar_numero()