
def run():
    numero = str ( input('Ingrese un numero para invertir: ') )
    numeroInve = []
    for i in numero:
        numeroInve.append (str(i))
    
    numeroInve = numeroInve[::-1]
    numeroInvertido = ''.join(numeroInve)
    
    print('El numero invertido es: {} '.format(numeroInvertido))

if __name__ == "__main__":
    run()