# -*- coding: utf-8

def run(empiezaSerie,cantidadSerie):
    fibonacci=[empiezaSerie]*cantidadSerie
    for i in range(cantidadSerie):
        if i == 0 or i == 1:
            fibonacci[i]=empiezaSerie
        else:
            fibonacci[i]=fibonacci[i-1] + fibonacci[i-2]
    
    for j in range(cantidadSerie):
        print("la serien ela posicion {} es: {}".format(j,fibonacci[j]))
        
    
    
if __name__ == "__main__":
    empiezaSerie = int(input("Introduce un numero donde quieras empezar la serie Fibonacci: "))
    cantidadSerie = int(input("Introduce un cantidad de la serie Fibonacci que quieres ver: "))
    run(empiezaSerie,cantidadSerie)