
def run():
    certamen1 = int(input('Ingresa la nota del certamen 1: '))
    certamen2 = int(input('Ingresa la nota del certamen 2: '))
    laboratorio = int(input('Ingresa la nota del laboratorio: '))
    c1c2nl = ( ( certamen1 * 0.7) / 3 ) + ( ( certamen2 * 0.7) / 3 ) + ( laboratorio * 0.3 )
    necesita = 0.7 / 3
    necesita = ( c1c2nl - 60 ) / necesita    
    necesita *= -1
    print('Necesita sacar mas de {} en el certamen 3'.format(round(necesita,1)))

    
if __name__ == "__main__":
    run()