
def run():
    anno = int ( input ("Ingrese el año: ") )
    if anno % 4 ==0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                print("El año {} es bisiesto ".format(anno))
            else:
                print("El año {} no es bisiesto ".format(anno))
        else:
            print("El año {} es bisiesto ".format(anno))
    else:
        print("El año {} no es bisiesto ".format(anno))            
    

if __name__ == "__main__":
    run()