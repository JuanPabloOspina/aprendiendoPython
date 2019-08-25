
def run():
    dividendo = int ( input("Ingrese el dividendo: ") )
    divisor = int ( input("Ingrese el divisor: "))
    resto = dividendo %  divisor
    cociente = dividendo /  divisor
    if  resto == 0:
        print ( "La division es exacta" )
        print ( "cociente: {} ".format(cociente) )
        print ( "resto: {} ".format(resto) )
    else:
        print ( "La division no es exacta" )
        print ( "cociente: {} ".format(cociente) )
        print ( "resto: {} ".format(resto) )
        

if __name__ == "__main__":
    run()