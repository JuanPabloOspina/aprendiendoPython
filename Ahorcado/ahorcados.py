import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


PALABRAS = [
    'lavadora',
    'arder',
    'funda',
    'costilla',
    'coral',
    'multa',
    'mordedura',
    'castigo',
    'bañarse',
    'crecer',
    'pensar',
    'america',
    'reunion',
    'perros',
    'gatos',
    'pajaros',
    'caballos',
    'peces',
    'humano',
    'hombre',
    'mujer',
    'niño',
    'niña'
]
def random_palabra():
    indice = random.randint(0, len(PALABRAS) - 1 )
    return PALABRAS[indice]

def patalla_vista(escondida_palabra,intentos):
    print(IMAGES[intentos])
    print('')
    print(escondida_palabra)
    print('--- * --- * --- * --- * --- * --- * --- * --- * --- * ---')

def run():
    palabra = random_palabra()
    escondida_palabra = ['-'] * len(palabra)
    intentos = 0

    while True:
        patalla_vista(escondida_palabra,intentos)
        carta_actual = input('Escribe una letra: ')

        indice_letra = []
        for idx in range(len(palabra)):
            if palabra[idx] == carta_actual:
                indice_letra.append(idx)
        
        if len(indice_letra) == 0:
            intentos += 1

            if intentos == 7:
                patalla_vista(escondida_palabra,intentos)
                print('')
                print('PERDISTE La palabra correcta era {}'.format(palabra))
                break

        else:
            for idx in indice_letra:
                escondida_palabra[idx] = carta_actual
            
            indice_letra = []

        try:
            escondida_palabra.index('-')
        except ValueError:
            print('')
            print('FELICIDADES Ganaste. La palabra es: {}'.format(palabra))
            break

if __name__ == "__main__":
    print("B I E N V E N I D O S  A A H O R C A D O S")
    run()