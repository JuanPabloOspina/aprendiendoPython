import random

def run():

    print("---ADIVINA EL LANZAMIENTO DE DOS DADOS---", "")
    number_found = False

    while not number_found:
        random_dice_1 = random.randint(1, 6)
        random_dice_2 = random.randint(1, 6)
        random_number_dices = [random_dice_1, random_dice_2]
        number_dice_1 = int(input('Digite el numero del dado 1: '))
        number_dice_2 = int(input('Digite el numero del dado 2: '))
        if number_dice_1 == random_dice_1 and number_dice_2 == random_dice_2:
            print('Felicidades. Adivinaste los dos dados')
            number_found = True
        else:
            print('Los dados arrojados fueron: ', random_number_dices)
            print("Inténtalo de nuevo. Lanzando de nuevo...")

if __name__ == '__main__':
    run()