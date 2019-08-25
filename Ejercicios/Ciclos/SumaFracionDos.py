
def run():
    n = int (input("Ingrese un numero: "))
    tabla = []
    potencia = 0
    frac = 0
    suma = 0

    for i in range(1,n+1):
        potencia = i 
        frac = 1/(2**i)
        suma += frac
        tabla.append([potencia,frac,suma])
    print ("Potencia --- Fraccion ----------- Suma")
    x=n
    c=0
    for i in range(n):
        if c < 9:
            print("{} ---------- {} --{} {}".format(tabla[i][0],tabla[i][1],"-"*(x-1),tabla[i][2] ))
            x-=1
            c+=1
        elif c >= 9:
            print("{} --------- {} --{} {}".format(tabla[i][0],tabla[i][1],"-"*(x-1),tabla[i][2] ))
            x-=1
            c+=1
    


if __name__ == "__main__":
    run()