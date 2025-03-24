# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 20:18:34 2025

@author: marce
"""

def cargar_nombres():
    dicNombres = {}
    try:
        with open('nombres.txt', 'r', encoding='utf8') as fp:
            for linea in fp:
                lineaLimpia = linea.strip()
                datosCliente = lineaLimpia.split(";")
                if len(datosCliente) == 2:
                    try:
                        dni = int(datosCliente[0].strip())  # Convertir el DNI a entero
                        nombre = datosCliente[1].strip()  # Obtener el nombre
                        dicNombres[dni] = nombre  # Agregar al diccionario
                    except ValueError:
                        print(f"Error en la línea: {lineaLimpia} - El DNI debe ser un número.")
    except FileNotFoundError:
        print("Error: El archivo 'nombres.txt' no se encuentra.")
    return dicNombres

def procesar_edades(dicNombres):
    try:
        with open('datos.txt', 'r', encoding='utf8') as fp:
            for linea in fp:
                lineaLimpia = linea.strip()
                datosCliente = lineaLimpia.split(";")
                if len(datosCliente) == 2:
                    try:
                        dni = int(datosCliente[0].strip())  # Convertir el DNI a entero
                        edad = int(datosCliente[1].strip())  # Obtener la edad
                        if dni in dicNombres:  # Comprobar si el DNI está en el diccionario
                            nombre = dicNombres[dni]  # Obtener el nombre
                            print(f"DNI: {dni} - Nombre: {nombre} - Edad: {edad}")
                        else:
                            print(f"DNI: {dni} no encontrado en el diccionario de nombres.")
                    except ValueError:
                        print(f"Error en la línea: {lineaLimpia} - El DNI o la edad no son números.")
    except FileNotFoundError:
        print("Error: El archivo 'edades.txt' no se encuentra.")

def main():
    dicNombres = cargar_nombres()  # Cargar los nombres en el diccionario
    if dicNombres:  # Verificar que el diccionario no esté vacío
        procesar_edades(dicNombres)  # Procesar las edades
    else:
        print("No se pudieron cargar los nombres.")

if __name__ == '__main__':
    main()

