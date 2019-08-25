
def run():
    numero = int (input("Ingrese el numero para general todas las potencias del 2 hasta N: "))
    for i in range(0,numero+1):
        result=(2**i)
        print(" 2 ** {} = {}".format(i,result))



if __name__ == "__main__":
    run()