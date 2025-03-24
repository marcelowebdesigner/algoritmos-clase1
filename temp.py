def contar_mayores_que_promedio(lista_edades, promedio):
    """ Retorna la cantidad de edades que están por encima del promedio """
    return sum(1 for edad in lista_edades if edad > promedio)

def main():
    edades = []  # Lista para almacenar las edades

    while True:
        edadStr = input("Ingrese una edad (o escriba 'salir' para terminar): ")

        if edadStr.lower() == "salir":  # Permite salir del bucle
            break

        edadInt = int(edadStr)

        while edadInt <= 0:  # Valida que la edad sea positiva
            print("Debe introducir una edad válida.")  
            edadStr = input("Ingrese una edad válida: ")
            edadInt = int(edadStr)

        edades.append(edadInt)  # Agrega la edad a la lista

        if 35 <= edadInt <= 45:
            print("Verdadero")  # Si está dentro del rango
        else:
            print("Falso")  # Si está fuera del rango

    # Si hay edades ingresadas, calcular estadísticas
    if edades:
        promedio = sum(edades) / len(edades)
        mayores_promedio = contar_mayores_que_promedio(edades, promedio)

        print(f"\nPromedio de edades ingresadas: {promedio:.2f}")
        print(f"Cantidad de edades por encima del promedio: {mayores_promedio}")
    else:
        print("No se ingresaron edades.")

if __name__ == "__main__":
    main()
