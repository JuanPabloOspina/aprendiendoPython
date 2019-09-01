
def run():
    numero = int (input('Ingrese un numero: '))
    suma = 0
    for i in range(numero + 1):
        suma += i

    sumaFormula = ( numero * ( numero + 1 ) ) / 2
    sumaFormula = int(sumaFormula)

    if suma == sumaFormula :
        print(' S1: {} y S2 {} Son Iguales.'.format(suma,sumaFormula))
    else:
        print(' S1: {} y S2 {} Son Diferentes.'.format(suma,sumaFormula))


if __name__ == "__main__":
    run()