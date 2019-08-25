
def run():
    numero1 = int (input ("Ingrese un numero: "))
    numero2 = int (input ("Ingrese un numero: "))
    resultado = 0
    
    if numero1 == numero2:
        print("La suma es 0")
    elif numero1 < numero2:
        numero2 = numero2 -1
        while numero1 != numero2:
            numero1 += 1
            resultado += numero1
        print("La suma es {} ".format(resultado))
    elif numero1 > numero2:
        numero1 = numero1 -1
        while numero2 != numero1:
            numero2 += 1
            resultado += numero2
        print("La suma es {} ".format(resultado))



if __name__ == "__main__":
    run()