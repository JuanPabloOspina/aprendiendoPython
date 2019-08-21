import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print("----*----*----*----*----*----*----*----*")
        print("Nombre: {}".format(contact.name))
        print("Telefono: {}".format(contact.phone))
        print("Email: {}".format(contact.email))
        print("----*----*----*----*----*----*----*----*")

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print("**********")
        print("¡No se encontró!")
        print("**********")

    def update_contact(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                case = str(input("""

                [n] = Actualizar Nombre
                [p] = Actualizar Telefono
                [e] = Actualizar e-mail
                [t] = Actualizar todo
                cualquier otra letra = salir de actualizar contactos

                """))

                if case == "n":
                    newName = str(input('Ingresa el nuevo nombre: ').lower())
                    newContact = Contact(newName, contact.phone, contact.email)
                    self._contacts[idx] = newContact
                    self._save()
                    print('Contacto actualizado')
                    break

                elif case == "p":
                    newPhone = str(input('Ingresa el nuevo numero telefonico: ').lower())
                    newContact = Contact(contact.name, newPhone, contact.email)
                    self._contacts[idx] = newContact
                    self._save()
                    print('Contacto actualizado')
                    break

                elif case == "e":
                    newEmail = str(input('Ingresa el nuevo email: ').lower())
                    newContact = Contact(contact.name, contact.phone, newEmail)
                    self._contacts[idx] = newContact
                    self._save()
                    print('Contacto actualizado')
                    break

                elif case == "t":
                    newName = str(input('Ingresa el nuevo nombre: ').lower())
                    newPhone = str(input('Ingresa el nuevo telefono: ').lower())
                    newEmail = str(input('Ingresa el nuevo email: ').lower())
                    newContact = Contact(newName, newPhone, newEmail)
                    self._contacts[idx] = newContact
                    self._save()
                    print('Contacto actualizado')
                    break
                else:
                    print("Saliendo...")
                    break

        else:
            self._not_found()


    def _save(self):
        with open("contacts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow( ("name", "phone", "email") )

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r', newline="") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0 or row == []:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])


    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input("Escribe el nombre del contacto:"))
            phone = str(input("Escribe el numero telefonico del contacto: "))
            email = str(input("Escribe el e-mail del contacto: "))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input("Escribe el nombre del contacto a actualizar:"))
            contact_book.update_contact(name)


        elif command == 'b':
            name = str(input("Escribe el nombre del contacto:"))

            contact_book.search(name)

        elif command == 'e':
            name = str(input("Escribe el nombre del contacto:"))

            contact_book.delete(name)

        elif command == 'l':

            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()