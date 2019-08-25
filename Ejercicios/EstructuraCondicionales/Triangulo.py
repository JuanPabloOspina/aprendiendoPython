
def run():
    a = float ( input("Ingrese el lado a:") )
    b = float ( input("Ingrese el lado b:") )
    c = float ( input("Ingrese el lado c:") )

    if a == b and a == c and b == c:
        print ("El triangulo es equilatero")
    elif a == c and a != b and c != b:
        print ("El triangulo es isosceles")
    elif a != b and a != c and b != c:
        print ("El triangulo es escaleno")

if __name__ == "__main__":
    run()