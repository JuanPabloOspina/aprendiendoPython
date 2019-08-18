# -*- codign: utf-8 -*-
def run():
    myString = raw_input("Ingrese un caracter para ver su ultima legra: ")
    print( myString[ len( myString) - 1 ])

    print(myString.upper())
    myString2 = myString.upper()
    print(myString2.lower())
    myString = 'edificio'
    print('mi string es: '+myString)
    print(myString.find('f'))
    print(myString[3])
    
    

if __name__ == "__main__":
    run()