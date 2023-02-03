def convertirNumeroBaseA(numeroEntrada, baseEntrada, baseSalida):
    """
    Esta función se basa en el algoritmo planteado por el ejercicio,
    sin embargo, solo es capaz de pasar un numero en base exclusivamente 
    decimal a otra base inferior.

    Parámetros:
    - numeroEntrada(int): es el numero al que se le va a hacer la conversion
    - baseEntrada(int): es la base del numero de entrada
    - baseSalida(int): es la base del numero convertido

    Devuelve:
    -numeroSalida(str): Es el resultado de la conversion 
    """
    numeroSalida = ''
    while numeroEntrada > 0:
        numeroSalida = str(numeroEntrada % baseSalida) + numeroSalida
        numeroEntrada = numeroEntrada // baseSalida
    return numeroSalida

#Para que pueda convertir un numero de cualquier base a otro numero de cualquier
#base es necesario hacer un paso adicional que consiste en pasar el numero de entrada
#a un numero en base 10

def convertirNumeroBaseB(numeroEntrada, baseEntrada, baseSalida):
    """
    Esta función puede convertir el numero de cualquier base a otra,
    siempre y cuando la base de entrada y de salida sea inferior a 10

    Parámetros:
    - numeroEntrada(int): es el numero al que se le va a hacer la conversion
    - baseEntrada(int): es la base del numero de entrada
    - baseSalida(int): es la base del numero convertido

    Devuelve:
    -numeroSalida(str): Es el resultado de la conversion 
    """
    numeroDecimal = 0
    numeroEntradaStr = str(numeroEntrada)
    potencia = len(numeroEntradaStr) - 1
    for digito in numeroEntradaStr:
        numeroDecimal += int(digito) * (baseEntrada ** potencia)
        potencia -= 1
    
    numeroSalida = ''
    while numeroDecimal > 0:
        numeroSalida = str(numeroDecimal % baseSalida) + numeroSalida
        numeroDecimal = numeroDecimal // baseSalida
    return numeroSalida

#A las funciones les hace falta rutinas de verificación, por ejemplo,
#si la base es 2 ningún dígito de la entrada debe ser mayor o igual a 2,
# por otro lado si hace conversiones a bases superiores, el problema es
# que las visualiza de forma inadecuada, por ejemplo: al pasar el numero
# decimal 2743 a hexadecimal en ves de imprimir AB7 imprime 10117, el 
#conjunto de dígitos 10 corresponde a A en HEX y el 11 corresponde a B en HEX
#por lo tanto si está haciendo correctamente la conversion.
#por otro lado en estas funciones no hay forma de introducir letras, por lo que
#no hay forma de ingresar valores superiores a base 10.

#python de forma nativa puede hacer este tipo de conversiones con la función int()

#conversion de los números 
numeroConvertidoA = convertirNumeroBaseA(287, 10, 4)
numeroConvertidoB = convertirNumeroBaseB(287, 10, 4)

#imprimir el resultado de la conversion
print("Resultado con la función A en base 4:")
print(numeroConvertidoA)
print("Resultado con la función B en base 4:")
print(numeroConvertidoB)