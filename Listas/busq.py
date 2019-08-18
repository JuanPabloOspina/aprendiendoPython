
def binary_search( number , number_usuario , low , high):

    if low > high:
        return False
    
    mid = int( ( low + high ) / 2 )

    if number[mid] == number_usuario:
        return True

    elif number[mid] > number_usuario:
        return binary_search( number , number_usuario , low , mid -1)

    else:
        return binary_search( number , number_usuario , low + 1 , high )

    

if __name__ == "__main__":
    number = [15,35,1,7,9,3,24,16,18,53,4]
    number_usuario = int(input("Ingresa un numero: "))
    number.sort()
    result = binary_search(number  , number_usuario , 0 , len( number ) - 1 )
    if result is True:
        print('El numero esta en la lista')
    else:
        print('El numero no esta en la lista')