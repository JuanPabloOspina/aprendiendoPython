def promedio(nota1, nota2, nota3, nota4):
    return ((nota1 + nota2 + nota3 + nota4) / 4)

def run():
    nota1 = float(input('Ingrese nota 1: '))
    nota2 = float(input('Ingrese nota 2: '))
    nota3 = float(input('Ingrese nota 3: '))
    nota4 = float(input('Ingrese nota 4: '))
    print('el promedio de las notas es: ', promedio(nota1, nota2, nota3, nota4))

if __name__ == "__main__":
    run()