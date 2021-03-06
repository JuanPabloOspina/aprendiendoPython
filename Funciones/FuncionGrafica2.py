# -*- coding: utf-8

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)
    turtle.mainloop()

def make_square(dave):
    length = int(input('Tamaño de cuadrado '))
    
    for i in range(6):
        make_line_and_turn(dave, length)
        dave.left(60)
        for i in range(3):
            make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(60)

if __name__ == "__main__":
    main()