from modulo_calculadora import *
# Iván Sacks Ejercicio Calculadora
# Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones: 
# 1. Ingresar 1er operando (A=x) 
# 2. Ingresar 2do operando (B=y) 
# 3. Calcular todas las operaciones 
# a) Calcular la suma (A+B) 
# b) Calcular la resta (A-B) 
# c) Calcular la división(A/B) 
# d) Calcular la multiplicación(A*B) 
# e) Calcular factorial(A!) 
# 4. Informar resultados 
# a) “El resultado de A+B es: r” 
# b) “El resultado de A-B es: r” 
# c) “El resultado de A/B es: r” o “No es posible dividir por cero” 
# d) “El resultado de A*B es: r” 
# e) “El factorial de A es: r1 y El factorial de B es: r2” 
# 5. Salir 
# • Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones  para realizar las cinco operaciones. 
# • En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,  se debe mostrar el número cargado) 
# • Deberán contemplarse los casos de error (división por cero, etc.) 
# • Documentar todas las funciones
calculadora = True
menu_opciones = ("Que desea hacer?\n"
                "1: Ingresar primer número\n"
                "2: Ingresar segundo número\n"
                "3: Calcular operaciones\n"
                "4: Informar resultados\n"
                "5: Salir\n")

res_1 = None
res_2 = None

while calculadora:
    opcion = input(menu_opciones)

    while not verificar_numero(opcion):
        opcion = input(menu_opciones)
    
    opcion = int(opcion)
    match opcion:
        case 1:
            x = input("Ingrese el primer operando ")
            while not verificar_numero(x):
                x = input("Reingrese el número ")

            x = int(x)
            pass
        case 2:
            y = input("Ingrese el segundo operando ")
            while not verificar_numero(y):
                y = input("Reingrese el número ") 

            y = int(y)
            pass
        case 3:
            try:
                operacion = input("Por favor, selecciona una operación: \n"
                    "1: Calcular la suma de {} + {}\n"
                    "2: Calcular la resta de {} - {}\n"
                    "3: Calcular la división de {} / {}\n"
                    "4: Calcular la multiplicación de {} * {}\n"
                    "5: Calcular factorial {}! y de {}!\n".format(x, y, x, y, x, y, x, y, x, y))
            except:
                print("Error, por favor, ingrese los números a operar en las opciones 1 y 2")
                break

            while not verificar_numero(operacion):
                operacion = input("Por favor, selecciona una operación: \n"
                    "1: Calcular la suma de {} + {}\n"
                    "2: Calcular la resta de {} - {}\n"
                    "3: Calcular la división de {} / {}\n"
                    "4: Calcular la multiplicación de {} * {}\n"
                    "5: Calcular factorial {}!\n".format(x, y, x, y, x, y, x, y, x))
            operacion = int(operacion)
            match operacion:
                case 1:
                    res_1 = suma(x, y)
                    signo = "suma"
                case 2:
                    res_1 = resta(x, y)
                    signo = "resta"
                case 3:
                    try:
                        res_1 = division(x, y)
                        signo = "división"
                    except:
                        print("Error, no se puede dividir entre cero")
                case 4:
                    res_1 = multiplicacion(x, y)
                    signo = "multiplicación"
                case 5:
                    try:
                        res_1 = factorial(x)
                        res_2 = factorial(y)
                        signo = "factorial"
                    except:
                        print("Error: No se pueden ingresar numeros no enteros o negativos para calcular un factorial")
                    
        case 4: 
            try:
                signo = signo
            except:
                print("Error: Para informar un resultado se necesita realizar una ecuación anteriormente")
                break

            match signo:
                case "suma":
                    print("El resultado de {0} + {1} es: {2}".format(x, y, res_1))
                case "resta":
                    print("El resultado de {0} - {1} es: {2}".format(x, y, res_1))
                case "división":
                    print("El resultado de {0} / {1} es: {2}".format(x, y, res_1))
                case "multiplicación":
                    print("El resultado de {0} * {1} es: {2}".format(x, y, res_1))
                case "factorial":
                    print("El factorial de {0} es: {1} y el factorial de {2} es: {3}".format(x, res_1, y, res_2))
            pass
        case 5:
            calculadora = False
            pass

