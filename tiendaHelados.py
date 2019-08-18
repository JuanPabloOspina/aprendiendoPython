def pagar(descuento,cuenta):
    paga = cuenta-(cuenta * descuento)
    print("El total a pagar es de ${}".format(paga))

def run(cuenta):
    membresia = int(input("Digite el tipo de membresia (1, 2 o 3): "))
    
    if membresia == 1:
        pagar(0.1,cuenta) 

    elif membresia == 2:
        pagar(0.1,cuenta)

    elif membresia == 3:
        pagar(0.1,cuenta)

    else:
        print("Error. Digite nuevamente")
        run(cuenta)

if __name__ == "__main__":
    cuenta = float(input("Digite el total de la cuenta: $"))
    run(cuenta)