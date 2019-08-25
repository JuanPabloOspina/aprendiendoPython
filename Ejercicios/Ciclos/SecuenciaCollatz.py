
def graficaCollatz(numero):
    
    
    bucle = True
    collatz = []
    collatz.append(numero)
    while bucle:
        if numero !=1:
            if (numero % 2) == 0:
                numero = numero/2
                collatz.append(int(numero))
            else:
                numero = (numero*3)+1
                collatz.append(int(numero))
        else:
            bucle = False
    
    for i in range(len(collatz)):
        print("{} {}".format(i+1,("*"*collatz[i])))

def listCollatz(numero):
    
    
    bucle = True
    collatz = []
    collatz.append(numero)
    while bucle:
        if numero !=1:
            if (numero % 2) == 0:
                numero = numero/2
                collatz.append(int(numero))
            else:
                numero = (numero*3)+1
                collatz.append(int(numero))
        else:
            print(collatz)
            bucle = False

def run():
    numero = int ( input("Ingrese un numero para sacar la secuencia de collatz: ") )
    listCollatz(numero)
    graficaCollatz(numero)

if __name__ == "__main__":
    run()