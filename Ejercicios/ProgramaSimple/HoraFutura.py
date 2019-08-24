def hora(nume):
    if nume < 12:
        return nume
    else:
        return hora(nume - 12)

def run():
    t = int(input('Ingrese la hora actual: '))
    h = int(input('Ingrese cantidad de horas: '))

    enT = t + h
    enT = hora(enT)
    
    print('En {} horas, el reloj marca las {}'.format(h,enT))

if __name__ == "__main__":
    run()