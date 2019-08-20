


def protected(func):

    def wrapper(*args, **rwargs):

        if password == 'platzi':
            return func(*args, **rwargs)
        else:
            print('Contraseña incorrecta.')

    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == "__main__":
    password = input('Ingresa tu contraseña: ')
    protected_func(password)