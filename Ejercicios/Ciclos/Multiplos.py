
def run():
    numero = int (input("Ingrese el numero para ver la trabla de multiplicar: "))
    for i in range(1,11):
        print(" {} * {} = {}".format(numero,i,(numero*i)))

if __name__ == "__main__":
    run()