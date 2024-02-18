'''
Problema 1
'''
#pip install request
import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()                  # Convertir la respuesta a formato JSON
        precio_usd = data['bpi']['USD']['rate_float']       # Obtener el precio de Bitcoin en USD
        return precio_usd
    except requests.RequestException as e:

        print("Error al obtener el precio de Bitcoin:", e)   # Manejar excepciones de solicitud
        return None

def main():

    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    precio_bitcoin_usd = obtener_precio_bitcoin()
    if precio_bitcoin_usd is not None:
        costo_usd = cantidad_bitcoins * precio_bitcoin_usd
        print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_usd:,.4f}")

if __name__ == "__main__":
    main()
'''
Problema 2
'''
#pip install pyfiglet
from pyfiglet import Figlet
import random

def imprimir_texto_con_fuente():
   
    figlet = Figlet()                       # Crear una instancia de Figlet
    fuentes_disponibles = figlet.getFonts() # Obtener la lista de fuentes disponibles

    nombre_fuente = input("Ingrese el nombre de una fuente o presione Enter para seleccionar una aleatoria: ").strip()
   
    if nombre_fuente == "":
        nombre_fuente = random.choice(fuentes_disponibles)
    else:
        # Verificar la disponibilidad de la fuente
        if nombre_fuente not in fuentes_disponibles:
            print("La fuente ingresada no está disponible. Seleccionando una aleatoria.")
            nombre_fuente = random.choice(fuentes_disponibles)

    figlet.setFont(font=nombre_fuente)

    texto = input("Ingrese el texto que desea imprimir: ")

    print(figlet.renderText(texto))

if __name__ == "__main__":
    imprimir_texto_con_fuente()
'''
Problema 3
'''
import requests
import zipfile
from io import BytesIO

url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_archivo_zip = "imagen.zip"
response = requests.get(url_imagen)

with zipfile.ZipFile(nombre_archivo_zip, 'w') as zip_file:  # Agregar la imagen descargada al archivo zip
    zip_file.writestr("imagen_descargada.jpg", response.content)

print("Imagen descargada y almacenada como archivo zip.")

with zipfile.ZipFile(nombre_archivo_zip, 'r') as zip_ref: # Descomprimimos el archivo zip
    zip_ref.extractall("imagen_descomprimida")            # Extraemos los contenidos del archivo zip

print("Archivo zip descomprimido exitosamente.")
'''
Problema 4
'''
import requests

def obtener_precio_bitcoin():
    try:
        # Realizar la solicitud a la API de CoinDesk
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # Convertir la respuesta a formato JSON
        data = response.json()
        # Obtener el precio de Bitcoin en USD
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        # Manejar excepciones de solicitud
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    # Solicitar al usuario la cantidad de bitcoins que posee
    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin_usd = obtener_precio_bitcoin()
    if precio_bitcoin_usd is not None:
        # Calcular el costo en USD de la cantidad de bitcoins
        costo_usd = cantidad_bitcoins * precio_bitcoin_usd
        # Mostrar el costo actual de la cantidad de bitcoins en USD
        print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_usd:,.4f}")
        # Abrir un archivo en modo anexar (append) para agregar datos al final del archivo
        with open('precio_bitcoin.txt', 'a') as archivo:
            # Escribir la cantidad de bitcoins, el precio de Bitcoin y el costo en USD en el archivo
            archivo.write(f"Cantidad de bitcoins: {cantidad_bitcoins}, Precio de Bitcoin (USD): {precio_bitcoin_usd:.2f}, Costo en USD: {costo_usd:,.4f}\n")
            print("Datos de precio de Bitcoin almacenados en 'precio_bitcoin.txt' correctamente.")

if __name__ == "__main__":
    main()

'''
Problema 5
'''
def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return
    
    with open(f"tabla-{numero}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{numero} x {i} = {numero*i}\n")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return
    
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            tabla = file.read()
            print(f"Tabla de multiplicar del {numero}:\n{tabla}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return
    
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if len(lineas) >= linea:
                print(f"Línea {linea} de la tabla del {numero}: {lineas[linea-1]}")
            else:
                print(f"La línea {linea} no existe en la tabla del {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\nMENU")
        print("1. Guardar tabla de multiplicar de un número.")
        print("2. Mostrar tabla de multiplicar de un número.")
        print("3. Mostrar línea de la tabla de multiplicar de un número.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea entre 1 y 10: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

'''
Problema 6
'''
def contar_lineas_codigo(archivo_path):
    try:
        with open(archivo_path, 'r') as archivo:
            lineas = archivo.readlines()

            # Filtrar líneas que no son comentarios ni líneas en blanco
            lineas_codigo = [linea.strip() for linea in lineas if not (linea.strip().startswith("#") or len(linea.strip()) == 0)]

            return len(lineas_codigo)
    except FileNotFoundError:
        print(f"El archivo {archivo_path} no fue encontrado.")
        return None

def main():
    try:
        ruta_archivo = input("Ingrese la ruta del archivo .py: ").strip()

        # Verificar si la ruta termina en '.py'
        if not ruta_archivo.endswith('.py'):
            print("El archivo no tiene extensión .py.")
            return

        cantidad_lineas = contar_lineas_codigo(ruta_archivo)

        if cantidad_lineas is not None:
            print(f"El archivo {ruta_archivo} tiene {cantidad_lineas} líneas de código (excluyendo comentarios y líneas en blanco).")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
'''
Problema 7
'''

'''
Problema 8
'''
    