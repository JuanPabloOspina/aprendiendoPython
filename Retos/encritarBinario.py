# -*- coding: utf-8 -*-

KEYS = {
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
    'G': '10000',
    'H': '10001',
    'I': '10010',
    'J': '10011',
    'K': '10100',
    'L': '10101',
    'M': '10110',
    'N': '10111',
    'O': '11000',
    'P': '11001',
    'Q': '11010',
    'R': '11011',
    'S': '11100',
    'T': '11101',
    'U': '11110',
    'V': '111111',
    'W': '100000',
    'X': '100001',
    'Y': '100010',
    'Z': '100011',
    '0': '0',
    '1': '1',
    '2': '10',
    '3': '11',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111',
    '8': '1000',
    '9': '1001',
    ' ': 'espace'
}

def cypher(message):
    message.upper()
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)


def decipher(message):
    message.upper()
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():

    while True:

        command = input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        ''')

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            break
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()