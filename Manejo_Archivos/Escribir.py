
def run():    
    with open('numeros.txt','w', encoding='utf-8') as archivo:
        for i in range(0,9):
            archivo.write(str(i))
            

if __name__ == "__main__":
    run()