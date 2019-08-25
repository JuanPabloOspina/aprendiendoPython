
def run():
    numero = int (input("Ingrese un numero para encontrar los divisores de este: "))
    div = []
    for i in range (1,(numero+1)):
        if (numero % i ) == 0:
            div.append(i)
    print("El numero {} es divisible por {}".format(numero,div))

if __name__ == "__main__":
    run()