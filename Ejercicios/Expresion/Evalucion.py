
def tipo(numero1):
    print(type(numero1))

def escribir(numero1):
    if numero1 == int:
        print("El Resultado Es: {} ".format(int(numero1)) )
    elif numero1 == str:
        print("El Resultado Es: {} ".format(str(numero1)) )

def suma(numero1, numero2):
    print(" S U M A")
    suma = numero1 + numero2 
    escribir(suma)
    print(type(suma))

def division(numero1, numero2):
    if numero2 == 0:
        print("La division por 0 no se puede realizar")
    else:
        div = numero1 / numero2
        print(" D I V I S I O N")
        escribir( div )
        print(type(div))
        
def sumaPorN(numero1,numero2,numero3):        
    resultado = numero1 + numero2 * numero3
    print("Suma de {} + {} * {} es : {} ".format( numero1, numero2, numero3, resultado ))
    escribir(resultado)
    tipo(resultado)

def sumaPorNString(string1, string2, numero1):
    resultado = ( string1 + string2 ) * numero1
    print("Suma de {} + {} * {} es : {} ".format( string1, string2, numero1, resultado ))
    escribir(resultado)
    tipo(resultado)

def igualMilCien(numero1):
    if ( (numero1 ** 10) == 1000 ):
        if ( (numero1 ** 7) == 100 ):
            resultado = numero1 ** 7
            print(" {} a la 7 ".format(int(numero1)))
            escribir(resultado)
            tipo(resultado)
        else:
            resultado = numero1 ** 10
            print(" {} a la 10 ".format(int(numero1)))
            escribir(resultado)
            tipo(resultado)
    else:
        print('El numero {} elevado a 7 - 10 no da como resultado 1000 - 100'.format(int(numero1)))

def cadenaNumerico(string1):
    try:
        resultado = int(string1)
        escribir(resultado)
        tipo(resultado)
    except ValueError as s:
        print('no se puede transformar {} en numerico '.format(string1))

def sumaDivisionSuma(numero1, numero2, numero3, numero4):
    if numero2 == 0:
        print("La division por 0 no se puede realizar")
    elif numero4 == 0:
        print("La division por 0 no se puede realizar")
    else:
        div = ( numero1 / numero2 ) + ( numero3 / numero4 )
        print(" D I V I S I O N  +  D I V I S I O N ")
        escribir( div )
        print(type(div))

def run():
    while True:
        resultado = int(input('''
                [1] Suma 
                [2] Division
                [3] Suma y por un numero N
                [4] Suma de dos string por un numero N
                [5] Elevado numero N por **7 o **10 con resultado 1000 o 100
                [6] Cadena de texto a numero
                [7] Suma Division Suma
                [8] Salir
        '''))
        if resultado == 1:
            numero1 = int(input('Ingrese un numero: '))
            numero2 = int (input('Ingrese otro numero: '))
            suma(numero1,numero2)

        elif resultado == 2:
            numero1 = int(input('Ingrese un numero: '))
            numero2 = int (input('Ingrese otro numero: '))
            division(numero1,numero2)

        elif resultado == 3:
            numero1 = int(input('Ingrese un numero: '))
            numero2 = int (input('Ingrese otro numero: '))
            numero3 = int (input('Ingrese otro numero: '))
            sumaPorN(numero1,numero2,numero3)

        elif resultado == 4:
            string1 = str(input('Ingrese un numero cadena: '))
            string2 = str(input('Ingrese otro numero cadena: '))
            numero1 = int (input('Ingrese un numero: '))
            sumaPorNString(string1,string2,numero1)

        elif resultado == 5:
            numero1 = int (input('Ingrese un numero: '))
            igualMilCien(numero1)

        elif resultado == 6:
            string1 = str(input('Ingrese un numero cadena: '))
            cadenaNumerico(string1)

        elif resultado == 7:
            numero1 = int(input('Ingrese un numero: '))
            numero2 = int (input('Ingrese otro numero: '))
            numero3 = int (input('Ingrese otro numero: '))
            numero4 = int (input('Ingrese otro numero: '))
            sumaDivisionSuma(numero1, numero2, numero3, numero4)

        elif resultado == 8:
            break

        else:
            print('Opcion no validad Escoja otra ')


if __name__ == "__main__":
    run()