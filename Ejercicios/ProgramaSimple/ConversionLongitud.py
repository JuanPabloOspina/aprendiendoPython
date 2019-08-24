
def run():
    centimetros = float(input('Ingrese los cm que quiere transformar en pulgadas: '))
    pulgadas = round((centimetros / 2.54),4)
    print('Las pulgadas son {} equivalente a {} cm '.format(pulgadas,centimetros))


if __name__ == "__main__":
    run()