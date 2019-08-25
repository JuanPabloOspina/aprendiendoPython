
def run():
    edad = int (input("Ingrese la edad: "))
    peso = float (input("Ingrese el peso en kg: "))
    altura = float (input("Ingrese la altura en m: "))

    mCorporal = peso / (altura ** 2)

    if edad < 45:
        if mCorporal < 22.0:
            print ("Riesgo de sufrir enfermeda coronaria es Baja ")
        else:
            print ("Riesgo de sufrir enfermeda coronaria es Medio ")
    elif edad >= 45:
        if mCorporal < 22.0:
            print ("Riesgo de sufrir enfermeda coronaria es Medio ")
        else:
            print ("Riesgo de sufrir enfermeda coronaria es Alto ")

if __name__ == "__main__":
    run()