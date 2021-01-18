# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Game(object):
    players = [];
    def __init__(self):
        print("Welcome to Connect Four Game!")
        print("Will you play (1) Human to Human, (2) Human to Computer or, (3) Computer to Computer?")
        gameTypeChoice = str(input("Please type 1, 2 or 3: "))

        self.players[0] = str(input("What is the name of player 1?"))
        self.players[1] = str(input("What is the name of player 2?"))

class Player(object):

    def __init__(self, name):




