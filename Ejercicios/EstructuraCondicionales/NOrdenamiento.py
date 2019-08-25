
def run():
    cantidadNumeros = int ( input("Cantidad N de ingreso numeros: ") )
    listaNumeros = []
    for i in range(cantidadNumeros):
        num = int ( input("Ingrese un numero: ") ) 
        listaNumeros.append(num)
        
    listaNumeros.sort()
    print("Lista con los numeros ordenados es: {} ".format(listaNumeros))

if __name__ == "__main__":
    run()