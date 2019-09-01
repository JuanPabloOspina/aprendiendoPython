

def run():
    numero = int ( input( 'Ingrese un numero: ' ) )
    numeroM = int ( input( 'Ingrese un numero: ' ) )
    cont = numeroM
    
    if numeroM == 1:
        resultado = numero

    if numeroM == 0:
        resultado = 1
    
    if numeroM > 1:
        resultado = numero
        for i in range(cont):
            resultado = resultado * ( numero + numeroM )
            numeroM -= 1

        


    print(resultado)


if __name__ == "__main__":
    run()