
def run():
    numero = int ( input( "Ingrese un numero a evaluar" ) )
    listaNumeros = []
    listaNumerosNo = []
    for i in range(numero):
        if (i % 3) != 0:
            if (i % 7) !=0:
                listaNumeros.append(i)
            else:
                listaNumerosNo.append(i)
        else:
                listaNumerosNo.append(i)
                
    print(' Numeros no multiplos 3-7 menores o iguales a {} son: {} '.format(numero,listaNumeros))
    print(' Numeros multiplos 3-7 menores o iguales a {} son: {} '.format(numero,listaNumerosNo))


if __name__ == "__main__":
    run()