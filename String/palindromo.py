def runing(palabra):
    reversa = palabra[::-1]
    if reversa == palabra:
        return True
    else:
        return False



def run(palabra):
    palabraNormal = []
    
    for letter in palabra:
        palabraNormal.insert(0,letter)

    palabraReves = ''.join(palabraNormal)

    if palabraReves == palabraNormal:
        return True
    else:
        return False
    

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    result = run(palabra)

    if result is True:
        print('{} si es una palindromo 1'.format(palabra))
    else:
        print('{} no es una palindromo 1'.format(palabra))

    print('')
    result = runing(palabra)

    if result is True:
        print('{} si es una palindromo'.format(palabra))
    else:
        print('{} no es una palindromo'.format(palabra))

    