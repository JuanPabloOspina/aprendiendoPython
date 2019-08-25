
def run ():
    matriz = []
    for i in range(0,11):
        matriz.append([])
        for j in range(0,11):
            matriz[i].append(i*j)


    for j in range(1,11):
        print(matriz[j])

    

if __name__ == "__main__":
    run()