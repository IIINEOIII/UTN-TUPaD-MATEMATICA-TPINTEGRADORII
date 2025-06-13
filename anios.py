# Importa función de verificación numérica desde el módulo 'dnis.py'
from dnis import verificador_digito_numerico

def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Funcion para solicitar y verificar años de nacimiento
def solicitar_anios():
    integrantes = int(input("Introduce el número de integrantes del grupo: "))
    anios = []
    for i in range(integrantes):
        anio = input(f"Introduce el año de nacimiento del integrante {i + 1}: ")
        if verificador_digito_numerico(anio) and len(anio) == 4:
            anios.append(int(anio))
        else:
            print("El año debe tener 4 dígitos numéricos.")
    return anios

# Funciones para realizar operaciones con los años de nacimiento
## Contar años bisiestos, verificar si todos nacieron después del 2000, calcular edades y producto cartesiano entre años y edades
def contar_bisiestos(anios):
    bisiestos = 0
    for anio in anios:
        if es_bisiesto(anio):
            bisiestos += 1
            print(f"Tenemos un año especial: el año {anio} es bisiesto.")
    print(f"El número de años bisiestos en el grupo es {bisiestos}")

def contar_posterior_2000(anios):
    posterior_2000 = []
    for anio in anios:
        if anio > 2000:
            posterior_2000.append(anio)
    if posterior_2000 == anios:
        print("Grupo Z: todos los integrantes del grupo nacieron después del 2000.")
    else:
        print("No todos los integrantes del grupo nacieron después del 2000.")

def calcular_edades(anios):
    edades = []
    for anio in anios:
        edad = 2025 - anio
        edades.append(edad)
    print(f"Las edades de los integrantes del grupo son: {edades}")
    return edades

def producto_cartesiano(anios):
    edades = calcular_edades(anios)
    producto = [(a, e) for a in anios for e in edades]
    print(f"El producto cartesiano entre los años y las edades es: {producto}")


# Función principal para ejecutar el programa
def main():
    print("Bienvenido al programa de análisis de años de nacimiento.")
    print("A continuación, se solicitarán los años de nacimiento con los que se trabajará.")
    anios = solicitar_anios()
    print("\nOperaciones disponibles:")
    print("1. Contar años bisiestos")
    print("2. ¿Todos nacieron después del 2000?")
    print("3. Calcular edades")
    print("4. Producto cartesiano entre años y edades")
    print("5. Salir")

    while True:
        print("\n----------------------")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == '1':
            contar_bisiestos(anios)
        elif opcion == '2':
            contar_posterior_2000(anios)
        elif opcion == '3':
            calcular_edades(anios)
        elif opcion == '4':
            producto_cartesiano(anios)
        elif opcion == '5':
            print("Saliendo del programa. ¡Nos vemos!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

# ejecuta la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()