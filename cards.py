import os, curses

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Cards:

    def __init__(self):
        pass

    def visual(self, mast, number, x, y):

        if mast == 1:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |     __  __     |
        |    (  \\/  )    |
        |     \\    /     |
        |      \\  /      |
        |       \\/       |
        |                |
        |                |
        | {number}            {number} |
        |________________|
        ''')
        elif mast == 2:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |       /\\       |
        |      /  \\      |
        |     /    \\     |
        |     \\    /     |
        |      \\  /      |
        |       \\/       |
        |                |
        | {number}            {number} |
        |________________|
        ''')
        elif mast == 3:
            return (f'''
         ________________
        | {number}            {number} |
        |       /\\       |
        |     /####\\     |
        |   /#########\\  |
        | (############) |
        |   \\########/   |
        |      |##|      |
        |     |####|     |
        | {number}            {number} |
        |________________|
        ''')

        elif mast == 4:
            return (f'''
         ________________
        | {number}            {number} |
        |                |
        |      ####      |
        |      ####      |
        | ############## |
        | ############## |
        |      ####      |
        |      ####      |
        |                |
        | {number}            {number} |
        |________________|
        ''')


cards = Cards()

print(cards.visual(1, 5, 20, 12))
print(cards.visual(3, 5, 40, 12))

