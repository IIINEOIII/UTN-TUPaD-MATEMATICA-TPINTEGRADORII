#FUNCIONES PARA OPERAR SOLICITAR Y VERIFICAR DNIs
#Generador de conjuntos a partir de un número
def verificador_digito_numerico(dni):
    for caracter in dni:
        if caracter not in "0123456789":    
            return False
    return True

def solicitar_dni():
    # Solicita un DNI al usuario hasta que se introduce uno válido 
    while True:
        dni = input("Introduce un DNI: ")
        if verificador_digito_numerico(dni) and len(str(dni)) == 8:
            return dni
        else:
            print("El número solo puede tener caracteres numéricos y debe tener 8 dígitos. Por favor, introduce un DNI válido.")

#FUNCIONES PARA OPERAR CON CONJUNTOS

# Función para generar un conjunto a partir de un DNI numérico
def generar_conjunto(dni):
    # Genera un conjunto de dígitos únicos a partir de un DNI numérico.
    # Devuelve False si el DNI no es numérico.
    conjunto = []
    for i in dni:
        if int(i) not in conjunto:
            conjunto.append(int(i))
    return sorted(conjunto)

#operaciones con conjuntos
def union_conjuntos(conjunto1, conjunto2):
    union = conjunto1
    for elemento in conjunto2:
        if elemento not in union:
            union.append(elemento)
    return sorted(union)

def interseccion_conjuntos(conjunto1, conjunto2):
    interseccion = []
    for e in conjunto1:
         if e in conjunto2:
            interseccion.append(e)
    return sorted(interseccion)

def diferencia_conjuntos(conjunto1, conjunto2):
    diferencia = []
    for e in conjunto1:
        if e not in conjunto2:
            diferencia.append(e)
    return sorted(diferencia)

def diferencia_simetrica_conjuntos(conjunto1, conjunto2):
    diferencia1 = diferencia_conjuntos(conjunto1, conjunto2)
    diferencia2 = diferencia_conjuntos(conjunto2, conjunto1)
    return sorted(diferencia1 + diferencia2)

def operar_con_conjuntos(conjunto1, conjunto2, operacion):
    if operacion == "union":
        return union_conjuntos(conjunto1, conjunto2)
    elif operacion == "interseccion":
        return interseccion_conjuntos(conjunto1, conjunto2)
    elif operacion == "diferencia":
        return diferencia_conjuntos(conjunto1, conjunto2)
    elif operacion == "diferencia_simetrica":
        return diferencia_simetrica_conjuntos(conjunto1, conjunto2)
    else:
        print("Operación no válida.")
    
#Programa para conjuntos de DNIs
def conjuntos_dnis():
    # Función principal el la que usuario genera los conjuntos correspondientes a los DNIs y realiza operaciones entre ellos.
    print("Bienvenido al generador de conjuntos a partir de DNIs.")
    print("Por favor, introducí dos DNIs para generar los conjuntos y realizar operaciones entre ellos.")    
    conjunto1 = generar_conjunto(solicitar_dni())
    conjunto2 = generar_conjunto(solicitar_dni())
    operacion = input("Introduce la operación (union, interseccion, diferencia, diferencia_simetrica): ").strip().lower()
    resultado = operar_con_conjuntos(conjunto1, conjunto2, operacion)
    if resultado is not None:
        print(f"El resultado de la operación {operacion} entre los conjuntos es:\nConjunto 1: {conjunto1} \nConjunto 2:{conjunto2}\n{operacion.capitalize()}: {resultado}")
    else:
        print("No se pudo realizar la operación.")


#FUNCION PARA SUMAR LOS DÍGITOS DE UN DNI
def sumar_digitos():
    dni= input("Introduce un DNI: ")
    if verificador_digito_numerico(dni) and len(str(dni)) == 8:
        suma = 0
        for caracter in dni:
            if caracter in "0123456789":
                suma += int(caracter)
        print(f"La suma de los dígitos del DNI {dni} es: {suma}")

#FUNCIÓN PARA CONTAR LA FRECUENCIA DE LOS DÍGITOS EN UN DNI
def contar_frecuencia_digitos():
    dni = solicitar_dni()
    frecuencia = {}
    for caracter in dni:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    print(f"La frecuencia de los dígitos en el DNI {dni} es: {frecuencia}")


#FUNCIONES PARA VERIFICAR EXPRESIONES LÓGICAS

#EXPRESIÓN LÓGICA 1: Función para determinar tendencia par en el grupo de DNIs de integrantes
def tendencia_par():
    integrantes = int(input("Introduce el número de integrantes del grupo: "))
    tendencias = []
    for i in range(integrantes):
        dni = input(f"Introduce el DNI del integrante {i + 1}: ")
        tendencias.append(verificar_tendencia_par(dni))
    if tendencias.count(True) == integrantes:
        print("El grupo de DNIs de los integrantes tiene tendencia par.")
    else:
        print("El grupo de DNIs de los integrantes no tiene tendencia par.")

def verificar_tendencia_par(dni):
    if verificador_digito_numerico(dni) and len(dni) == 8:
        pares = 0

        for caracter in dni:
            if int(caracter) % 2 == 0:
                pares += 1
        if pares > 0:
            return True
        else:
            return False
    else:
        print("El número solo puede tener caracteres numéricos y debe tener 8 dígitos.")

#EXPRESIÓN LÓGICA 2: Función para determinar si existe una unión completa entre dos conjuntos de DNIs
def union_completa():
    integrantes = int(input("Introduce el número de integrantes del grupo: "))
    union = []
    for i in range(integrantes):
       conjunto = generar_conjunto(solicitar_dni())
       for e in conjunto:
           if e not in union:
               union.append(e)
    if len(union) == 10:  # Si la unión tiene todos los dígitos del 0 al 9
        print("Existe una unión completa entre los conjuntos de DNIs, ya que contiene todos los dígitos del 0 al 9.")
    else:
        print("No existe una unión completa entre los conjuntos de DNIs, ya que falta alguno de los dígitos del 0 al 9.")


#EXPRESIÓN LÓGICA 3: Función para determinar si existen elementos extremos (0 o 9) en al menos uno de los conjuntos de DNIs

def extremos_en_conjuntos():
    integrantes = int(input("Introduce el número de integrantes del grupo: "))
    union = []
    for i in range(integrantes):
        conjunto = generar_conjunto(solicitar_dni())
        for e in conjunto:
            if e not in union:
                union.append(e)
    if "0" in union or "9" in union:
        print("Existen elementos extremos (0 o 9) en al menos uno de los conjuntos de DNIs.")
    else:
        print("No existen elementos extremos (0 o 9) en los conjuntos de DNIs.")

# FUNCIÓN PARA EJECUTAR EL PROGRAMA PRINCIPAL
def main():
    while True:
        print("\nOpciones:")
        print("1. Operar con conjuntos a partir de DNIs")
        print("2. Sumar dígitos de un DNI")
        print("3. Contar frecuencia de dígitos en un DNI")
        print("4. Verificar tendencia par en un grupo de DNIs")
        print("5. Verificar unión completa entre conjuntos de DNIs")
        print("6. Verificar existencia de elementos extremos (0 o 9) en conjuntos de DNIs")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            conjuntos_dnis()
        elif opcion == "2":
            sumar_digitos()
        elif opcion == "3":
            contar_frecuencia_digitos()
        elif opcion == "4":
            tendencia_par()
        elif opcion == "5":
            union_completa()
        elif opcion == "6":
            extremos_en_conjuntos()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intenta nuevamente.")

if __name__ == "__main__":
    main()