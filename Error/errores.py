contries = {
    'mexico':122,
    'colombia':49,
    'argentina':43,
    'chile':18,
    'peru':31
}

while True:
    contry = input("Escriba el nombre de un pais: ").lower()
    
    try:
        print("la poblacion de {} es: {} millones".format(contry,contries[contry]))    
    except KeyError:
        print('no tenemos el dato de la poblacion de {}'.format(contry))
    
        
    
