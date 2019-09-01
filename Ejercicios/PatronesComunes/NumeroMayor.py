
def run():
    n = int (input('Ingrese n: '))
    numeros = []
    for i in range(n):
        numero = int ( input ( 'Ingrese un numero: ' ) )
        numeros.append(numero)
    numeros.sort()
    numeros.reverse()
    print('numero mayor es {} '.format(numeros[0]))

if __name__ == "__main__":
    run()