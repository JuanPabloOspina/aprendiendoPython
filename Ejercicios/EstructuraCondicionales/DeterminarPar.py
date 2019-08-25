
def run ():
    numero = int ( input ("Ingrese el numero para saber si es par: ") )
    if numero % 2 == 0:
        print("El numero {} es par".format(numero))
    else:
        print("El numero {} es impar".format(numero))
if __name__ == "__main__":
    run()