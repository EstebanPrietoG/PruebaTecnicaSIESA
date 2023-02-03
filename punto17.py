def dividir(dividendo, divisor):
    """
    Divide dos números, pueden ser flotantes o enteros

    Parámetros:
    - dividendo(float): el numero que se quiere dividir
    - divisor(float): el numero que va a dividir al otro

    Devuelve:
    - resultado(float): el resultado de la division
    """
    return dividendo/divisor

def dividirEnteros(dividendo, divisor):
    """
    Divide dos números, solo pueden ser números enteros

    Parámetros:
    - dividendo(int): el numero que se quiere dividir
    - divisor(int): el numero que va a dividir al otro

    Devuelve:
    - resultado(float): el resultado de la division
    """

    try:
        if not isinstance(dividendo, int) or not isinstance(divisor, int):
            raise TypeError
        return dividendo//divisor
    except TypeError:
        print("Error: no se introdujeron datos enteros")
        return "Error"
#dejo que python maneje el error de division por cero en ambos casos

#Divide e imprime las divisiones
print(dividir(23,2))
print(dividirEnteros(12,4))
