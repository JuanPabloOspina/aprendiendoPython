
def run ():
    a = True
    totalMinutos = 0
    while a:
        tiempo = int(input("Ingrese duracion del tramo: "))
        if tiempo == 0:
            a = False
        else:
            totalMinutos += tiempo
    
    auxMinutos =(totalMinutos % 10 )
    
    totalMinutos = totalMinutos-auxMinutos

    auxTotalMinutos = totalMinutos

    a=True
    while a:
        if auxTotalMinutos < 60:

            auxMinutos+=auxTotalMinutos


            totalHora =  (totalMinutos * 0.0166667)
            a=False
        else:
            auxTotalMinutos -= 60

    if auxMinutos % 10 < 1:
        auxMinutos= auxMinutos % 10 
    
    print("Hora {} con {} minutos".format((round(totalHora)), auxMinutos))
    print


if __name__ == "__main__":
    run()