import math

def run():
    numero = float(input('Ingrese el numero para sacar el decimal: '))
    parte_decimal, parte_entera = math.modf(numero)
    print("Su parte decimal es {}".format(parte_decimal))

if __name__ == "__main__":
    run()