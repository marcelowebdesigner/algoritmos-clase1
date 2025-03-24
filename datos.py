# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 20:14:20 2025

@author: marce
"""

def main():
    with open('datos.txt', 'r', encoding='utf8') as fp:  # Abrir el archivo en modo lectura
        for linea in fp:
            lineaLimpia = linea.strip()  # Eliminar espacios, tabulaciones, saltos de línea
            datosCliente = lineaLimpia.split(";")  # Dividir la línea por el separador ";"

            # Solo procesar líneas con exactamente dos elementos
            if len(datosCliente) == 2:
                try:
                    dni = int(datosCliente[0].strip())  # Convertir el DNI a entero
                    edad = int(datosCliente[1].strip())  # Convertir la edad a entero
                    print(f"DNI: {dni} Edad: {edad}")
                except ValueError:
                    print(f"Error: Los datos en la línea '{lineaLimpia}' no son válidos. DNI y edad deben ser enteros.")
            
# Llamamos a la función principal
if __name__ == '__main__':
    main()
