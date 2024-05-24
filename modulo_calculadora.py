def verificar_numero(dato):
    """Verifica si un dato es un nomero

    Args:
        dato (int): Un numero real

    Returns:
        bool: El dato verificado
    """
    numero = None

    if dato.isdigit():
        numero = True
    else:
        numero = False

    return numero


def suma(num1: float, num2: float)-> float:
    """Suma dos números

    Args:
        num1 (float): Un número real
        num2 (float): Un número real

    Returns:
        float: El resultado de la suma de los argumentos
    """
    return num1 + num2

def resta(num1: float, num2: float)-> float:
    """Resta dos números

    Args:
        num1 (float): Un número real
        num2 (float): Un número real

    Returns:
        float: El resultado de la resta de los argumentos
    """
    return num1 - num2

def division(num1: float, num2: float)-> float:
    """Divide dos números

    Args:
        num1 (float): Un número real
        num2 (float): Un número real

    Returns:
        float: El resultado de la división de los argumentos
    """
    return num1 / num2

def multiplicacion(num1: float, num2: float)-> float:
    """Multiplica dos números

    Args:
        num1 (float): Un número real
        num2 (float): Un número real

    Returns:
        float: El resultado de la multiplicación de los argumentos
    """
    return num1 * num2


def factorial(num1: int)-> int:
    """Calcula el factorial de un número

    Args:
        num1 (int): Un número real

    Returns:
        float: El resultado del factorial de un número
    """
    factorial = 1
    for i in range(2, num1 + 1):
        factorial *= i
    
    return factorial

