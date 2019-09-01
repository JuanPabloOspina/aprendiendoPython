

def run():
    numero = int ( input ( 'Ingrese un numero para factorial: ' ) )
    i = 0
    while i != (numero + 1):
        if i == 0:
            factorial = 1
        else:
            factorial *= i 
        i += 1
    print(factorial)

if __name__ == "__main__":
    run()