class Contacto:

    def __init__ (self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

class LibroContacto:

    def __init__(self):
        self._contacts = []

    def add(self,name,phone,email):
        print('name: {}, phone: {}, email: {}'.format(name,phone,email))



def run():
    libro_contacto = LibroContacto()

    while True:
        Command = str(input('''
            Que desea hacer?

            [a]dd contact
            [u]pdate contact
            [s]earch contact
            [d]elete contact
            [t]o list contacts
            [e]xit program

            '''))

        if Command == 'a':
            name = str(input('Ingresa el nombre del contacto: '))
            phone = str(input('Ingresa el telefono del contacto: '))
            email = str(input('Ingresa el email del contacto: '))

            libro_contacto.add(name,phone,email)

        elif Command == 'u':
            print(' ')

        elif Command == 's':
            print(' ')

        elif Command == 'd':
            print(' ')

        elif Command == 't':
            print(' ')

        elif Command == 'e':
            print(' ')
            break

        else:
            print('Has copiado {} y no es una opcion correcta'.format(Command))
            

            


if __name__ == "__main__":   
    print('   B I E N V E N I D @  A  L A  A G E N D A') 
    run()