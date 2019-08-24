import math

def run():
    radio = float(input('Ingrese el radio de un circulo: '))
    perimetro = round( ((radio * 2) * math.pi), 1 )
    area = round( ((radio**2) * math.pi), 1 )
    print('El perimetro del circulo es {} '.format(float(perimetro)))
    print('El area del circulo es {} '.format(float(area)))

if __name__ == "__main__":
    run()