# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    col_to_usa_rate= 0.00029
    return ammount * col_to_usa_rate

def run():
    print("C A L C U L A D O R A  D E  D I V I S A")
    print ("convierte de pesos colombianos a dolar americano")
    print("")    
    ammount = float(input("Cantidad de pesos Colombianos para convertir"))
    result = foreign_exchange_calculator(ammount)
    print('${} pesos colombianos son ${} dolar americanos'.format(ammount, result))


if __name__ == "__main__":
    run()