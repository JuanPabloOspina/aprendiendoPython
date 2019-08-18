
def run(temps):
    sumaTemperaturas=0
    for temp in temps:
        sumaTemperaturas += temp

    return sumaTemperaturas / len(temps)


if __name__ == "__main__":
    temps = [21,25,18,29,23,24,26]
    print('La temperatura promedio es: {} '.format(run(temps)))