
def run(palabra):
    aux = []
    contador = 0
    j=0
    with open('./aleph.txt','r', encoding='utf-8') as archivo:
        for line in archivo:
            j+=1
            if line.count(palabra):
                contador += line.count(palabra)
                aux.append(j)

    print('{} se encuenta {} en el texto'.format(palabra,contador))
    print('Sen encuentra en {} diferentes parrafos por todo el texto'.format(aux))
    

if __name__ == "__main__":
    palabra = input('Ingresa la palabra que quieres saber cuantas veces esta en el archivo aleph.txt: ')
    run(palabra)