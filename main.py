from gui import *


def main():
    """
    Method used to set the dimensions of the window of the game of rock, paper, scissors
    """
    window = Tk()
    window.title("Rock, Paper, Scissors")
    window.geometry("300x120")
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    """
    Calls the function main in order to start the game
    """
    main()
