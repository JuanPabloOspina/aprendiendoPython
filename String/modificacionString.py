# -*- coding: utf-8 -*-

def run():
    s = 'hola'
    r = 'l' + s[1:] 
    print(r)
    print('')
    nombre1 = 'lola'
    nombre2 = 'mariana'
    print(nombre1 == nombre2)
    print(nombre1 == nombre1)
    print(nombre1 > nombre2)
    print(nombre1 < nombre2)

if __name__ == "__main__":
    run()