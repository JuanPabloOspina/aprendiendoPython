


class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on= is_turned_on
        self._display_img()

    def turn_on(self):
        self._is_turned_on= True
        self._display_img()

    def turn_off(self):
        self._is_turned_on=False
        self._display_img()

    def _display_img(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
    
def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        ''')
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            break
        else:
            print('*--* Invalida *--*')
            

if __name__ == "__main__":
    run()