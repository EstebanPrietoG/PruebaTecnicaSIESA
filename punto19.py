# Estructura del árbol con funciones para crearlo o copiarlo

class Arbol:
    """
    Clase de la estructura del árbol

    Atributos:

    - peso (int): Es el peso de la raíz del árbol
    - subArboles (list): Es la lista de los subArboles del árbol principal

    Métodos:

    - agregarSubArbol: agrega un subÁrbol al árbol
    - copiar: Hace una copia del árbol
    """
    def __init__(self, peso):
        self.peso = peso
        self.subArboles = []
    
    def agregarSubArbol(self, subArbol):
        """
        Agrega un subÁrbol al árbol

        Parámetros:
        - subArbol (arbol): el subArbol(que es un árbol) a agregar
        """
        self.subArboles.append(subArbol)

    def copiar(self):
        """
        Hace la copia del árbol

        Devuelve:
        - arbol(arbol): devuelve la copia del árbol
        """
        arbolNuevo = Arbol(self.peso)
        for subArbol in self.subArboles:
            arbolNuevo.agregarSubArbol(subArbol.copiar())
        return arbolNuevo

#Funciones para hacer cálculos con el arbol o visualizarlo

#Hice esta función para poder depurar los arboles
def print_tree(arbol, nivel):
    """
    Imprime el arbol

    Parámetros:
    - arbol(arbol): el arbol que se requiere imprimir
    - nivel(int): el nivel del arbol desde el cual se requiere imprimir
    """
    print("  " * nivel + str(arbol.peso))
    for subArbol in arbol.subArboles:
        print_tree(subArbol, nivel + 1)

def sumarPesos(arbol):
    """
    Suma cada uno de los pesos del arbol para obtener el peso total

    Parámetros:
    - arbol(arbol): el arbol que se va a obtener los pesos

    Devuelve:
    - sum(int): la suma total del arbol
    """
    sum = arbol.peso
    for subArbol in arbol.subArboles:
        sum += sumarPesos(subArbol)
    return sum

def sumarContarPesos(arbol):
    """
    Suma cada uno de los pesos del arbol para obtener el peso total
    y cuenta la cantidad de subArboles que hay en el arbol

    Parámetros:
    - arbol(arbol): el arbol que se va a obtener los pesos

    Devuelve:
    - suma(int): la suma total del arbol
    - contador(int): la cantidad total de arboles y subArboles
    """
    suma = arbol.peso
    contador = 1
    for subArbol in arbol.subArboles:
        sumaSubArbol, contadorSubArbol = sumarContarPesos(subArbol)
        suma += sumaSubArbol
        contador += contadorSubArbol
    return suma, contador

def promedioPesos (arbol):
    """
    Obtiene el promedio de los pesos del arbol

    Parámetros:
    - arbol(arbol): el arbol que se va a obtener el promedio

    Devuelve:
    - promedio (float): es el resultado entre dividir la suma total
    de los pesos y el el numero de subArboles, lo que daría el promedio
    """
    suma, contador = sumarContarPesos(arbol)
    return suma/contador

def alturaArbol(arbol):
    """
    Obtiene la altura del arbol

    Parámetros:
    - arbol(arbol): el arbol que se va a obtener la altura

    Devuelve:
    - altura(int): la altura total del arbol
    """
    if not arbol.subArboles:
        return 1
    return 1 + max(alturaArbol(subArbol) for subArbol in arbol.subArboles)

#Construcción de los arboles

#Arbol 1
arbol1 = Arbol(4)

#Arbol 2
arbol2 = arbol1.copiar()
subArbol1 = Arbol(1)
subArbol2 = Arbol(2)
arbol2.agregarSubArbol(subArbol1)
arbol2.agregarSubArbol(subArbol2)

#Arbol 3
subArbol3 = subArbol2.copiar()
subArbol3.agregarSubArbol(Arbol(3))
subArbol4 = Arbol(5)
subArbol4.agregarSubArbol(subArbol1)
subArbol4.agregarSubArbol(Arbol(4))
arbol3 = arbol1.copiar()
arbol3.agregarSubArbol(subArbol1)
arbol3.agregarSubArbol(subArbol3)
arbol3.agregarSubArbol(subArbol4)

#Obtiene los datos de los arboles
pesoArbol1 = sumarPesos(arbol1)
pesoArbol2 = sumarPesos(arbol2)
pesoArbol3 = sumarPesos(arbol3)

promedioArbol1 = promedioPesos(arbol1)
promedioArbol2 = promedioPesos(arbol2)
promedioArbol3 = promedioPesos(arbol3)

alturaArbol1 = alturaArbol(arbol1)
alturaArbol2 = alturaArbol(arbol2)
alturaArbol3 = alturaArbol(arbol3)


#Imprime los datos de los arboles
print("Las características del arbol 1 son las siguientes:")

print("Peso:", pesoArbol1)
print("Promedio:", promedioArbol1)
print("Altura:", alturaArbol1)

print("Las características del arbol 2 son las siguientes:")

print("Peso:", pesoArbol2)
print("Promedio:", promedioArbol2)
print("Altura:", alturaArbol2)

print("Las características del arbol 3 son las siguientes:")

print("Peso:", pesoArbol3)
print("Promedio:", promedioArbol3)
print("Altura:", alturaArbol3)