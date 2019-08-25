
def cuadrado(altura,ancho):
    for i in range(altura):
        print(" * "*ancho)

def triangulo(altura):
    auxiliar = 0
    for i in range(altura):
        auxiliar+=1
        print(" * "*auxiliar)

def hexagono(lado):
    aux1=(lado*2)-1
    aux2=int(aux1/2)
    aux3=aux2
    lados = lado
    
    
    
    for i in range(aux2):
        print("  "*aux2," *"*lados)
        aux2 -=1
        lados +=2
    print("  "*aux2," *"*lados)
    aux2 +=1
    lados -=2
    
    for j in range(aux3):
        print("  "*aux2," *"*lados)
        aux2 +=1
        lados -=2
        
            

def run():
    cuadrado(3,5)
    print(" ")
    triangulo(5)
    print(" ")
    hexagono(8)

if __name__ == "__main__":
    run()