def run(numero):
    if numero == 0:
        return 1
    return numero * run(numero-1)

if __name__ == "__main__":
    numero = int(input('Digite numero para fatorial: '))
    result = run(numero)
    print (result)