
def run():
    palabra1 = str ( input("Ingrese la palabra 1: ") )
    palabra2 = str ( input("Ingrese la palabra 2: ") )
    cantidadP1 = len(palabra1)
    cantidadP2 = len(palabra2)

    if cantidadP1 == cantidadP2:
        print("Las dos palabras tienen la misma cantidad de letras {} ".format(cantidadP1))
    elif cantidadP1 > cantidadP2:
        resul = cantidadP1 - cantidadP2
        print("La palabra {} tiene {} letras mas que la palabra {} ".format(palabra1,resul,palabra2))
    else:
        resul = cantidadP2 - cantidadP1
        print("La palabra {} tiene {} letras mas que la palabra  {} ".format(palabra2,resul,palabra1))

if __name__ == "__main__":
    run()