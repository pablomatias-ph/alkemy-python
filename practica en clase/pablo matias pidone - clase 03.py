def funcionsuma(num01, num02):
    return num01 + num02

def funciondivision(num01, num02):
    if num01 == 0 or num02 == 0:
        return "Los valores deben ser distintos a 0"
    else:
        return num01 / num02

def aritmeticasimple():
    accion = int(input("\nSi desea sumar dos números indique '1'\n"
                       "Si desea dividir dos números indique '2'\n"
                       "Para salir presione otro numero: "))
    while accion != 1 or accion != 2:
        if accion == 1:
            num01 = int(input("\nIngrese primer término: "))
            num02 = int(input("Ingrese segun término: "))
            funcionsuma(num01, num02)
            print(funcionsuma(num01, num02))
            accion = int(input("\nSi desea sumar dos números indique '1'\n"
                               "Si desea dividir dos números indique '2'\n"
                               "Para salir presion otro numero: "))
        elif accion == 2:
            num01 = int(input("\nIngrese el dividendo: "))
            num02 = int(input("Ingrese el divisor: "))
            print(funciondivision(num01, num02))
            accion = int(input("\nSi desea sumar dos números indique '1'\n"
                               "Si desea dividir dos números indique '2'\n"
                               "Para salir presion otro numero: "))
        else:
            return False
aritmeticasimple()