import math

def run():
    a = float(input('Ingresa el cateto a: '))
    b = float(input('Ingresa el cateto b: '))
    c = math.sqrt((a**2)+(b**2))
    print('La hipotenusa es: {}'.format(c))

if __name__ == "__main__":
    run()