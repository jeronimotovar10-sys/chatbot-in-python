import os
from datetime import datetime
from colorama import init
init()

import random
def tirar_dado():
    numero = random.randint(1, 6)
    return f"salio el numero: {numero}"

RESET = "\033[0m"
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"

ARCHIVO_NOMBRE = "nombre.txt"
ARCHIVO_APRENDIZAJE = "aprendizaje.txt"
ARCHIVO_EDAD = "edad.txt"

print(AZUL + "hola, soy tu chatbot en python" + RESET)
print(ROJO + "Escribe 'adios' cuando quieras terminar" + RESET)

nombre = ""
edad = ""

# Cargar nombre
if os.path.exists(ARCHIVO_NOMBRE):
    with open(ARCHIVO_NOMBRE, "r", encoding="utf-8") as archivo:
        nombre = archivo.read().strip()

# Cargar aprendizaje
aprendizaje = {}
if os.path.exists(ARCHIVO_APRENDIZAJE):
    with open(ARCHIVO_APRENDIZAJE, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if "=" in linea:
                pregunta, respuesta = linea.strip().split("=", 1)
                aprendizaje[pregunta] = respuesta

# Cargar edad
if os.path.exists(ARCHIVO_EDAD):
    with open(ARCHIVO_EDAD, "r", encoding="utf-8") as archivo:
        edad = archivo.read().strip()


while True:
    mensaje = input(AZUL + "Tu: " + RESET).lower().strip()

    # Respuestas aprendidas
    if mensaje in aprendizaje:
        print(VERDE + f"Bot: {aprendizaje[mensaje]}" + RESET)
        continue

    # Respuestas programadas
    if "hola" in mensaje:
        print(VERDE + "Bot: hola, ¿cómo estás?" + RESET)

    elif mensaje == "bien":
        print(AMARILLO + "Bot: me alegra saberlo" + RESET)

    elif mensaje == "mal":
        print(ROJO + "Bot: siento eso, espero que tu día mejore" + RESET)

    elif mensaje == "como te llamas":
        print(AMARILLO + "Bot: me llamo Subaru" + RESET)

    elif mensaje == "que puedes hacer":
        print(AZUL + "Bot: puedo responder mensajes simples, aprender y decir la hora" + RESET)

    elif mensaje in ["quien es tu creador", "cual es tu creador"]:
        print(AMARILLO + "Bot: fue jeronimo" + RESET)

    elif mensaje == "que cosas te gustan":
        print(AZUL + "Bot: me gustan los videojuegos" + RESET)

    elif mensaje == "eres real":
        print(AMARILLO + "Bot: soy tan real como tu imaginación" + RESET)

    # Guardar nombre
    elif mensaje.startswith("me llamo"):
        nombre = mensaje.replace("me llamo", "").strip()
        print(VERDE + f"Bot: mucho gusto, {nombre}" + RESET)
        with open(ARCHIVO_NOMBRE, "w", encoding="utf-8") as archivo:
            archivo.write(nombre)

    elif mensaje in ["cual es mi nombre", "mi nombre es"]:
        if nombre != "":
            print(VERDE + f"Bot: tu nombre es {nombre}" + RESET)
        else:
            print(AMARILLO + "Bot: aun no se tu nombre. Dime 'me llamo ...' " + RESET)

    # Guardar edad
    elif mensaje.startswith("tengo"):
        posible_edad = mensaje.replace("tengo", "").strip()
        if posible_edad.isdigit():
            edad = posible_edad
            with open(ARCHIVO_EDAD, "w", encoding="utf-8") as archivo:
                archivo.write(edad)
            print(VERDE + f"Bot: entendido, tienes {edad} años." + RESET)
        else:
            print(ROJO + "Bot: esa no parece una edad válida." + RESET)

    elif mensaje == "cual es mi edad":
        if edad != "":
            print(VERDE + f"Bot: tu edad es {edad} años." + RESET)
        else:
            print(AMARILLO + "Bot: aun no me has dicho tu edad." + RESET)

    #hora
    elif mensaje in ["hora", "que hora es", "¿que hora es?", "qué hora es"]:
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(AMARILLO + f"Bot: la hora actual es {hora_actual}" + RESET)
        
    #juego dado
    elif mensaje == "tirar dado" or mensaje == "dado" or mensaje == "jugar dado":
        print(VERDE + "Bot: " + tirar_dado() + RESET)
    # Salida
    elif mensaje in ["salir", "adios"]:
        print(ROJO + "Bot: adios" + RESET)
        break

    # Aprendizaje nuevo
    else:
        print(ROJO + "Bot: no se responder a eso" + RESET)
        nuevo_respuesta = input(AMARILLO + "Enseñame que responder: " + RESET).strip()
        aprendizaje[mensaje] = nuevo_respuesta
        with open(ARCHIVO_APRENDIZAJE, "a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}={nuevo_respuesta}\n")
        print(VERDE + "Aprendido para la proxima vez" + RESET)
