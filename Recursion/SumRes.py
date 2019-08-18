def operar(numero1, numero2):
    if(numero2 == 0):
        return numero1
    elif(numero2 < 0):
        return operar(numero1-1, numero2+1)
    else:
        return operar(numero1+1, numero2-1)
 
 
if __name__ == "__main__":
    print('Los numeros pueden ser negativos')
    primerNumero = int(input('Ingrese el primer numero para Sumar/Restar: '))
    segundoNumero = int(input('Ingrese el segundo numero para Sumar/Restar: '))
    print('Sumando {} y {}:'.format(primerNumero,segundoNumero), operar(primerNumero, segundoNumero))
    