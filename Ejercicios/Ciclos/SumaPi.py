
def run():
    n = int ( input("Ingrese el numero n para la suma: ") )
    sum=1
    aux=3
    rotador = True
    for i in range(1,n):
        if rotador:
            sum= sum - (1/(aux))
            rotador=False
            aux+=2
        else:
            sum= sum + (1/(aux))
            rotador=True
            aux+=2

    sumPi=4*sum

    print(sumPi)

if __name__ == "__main__":
    run()