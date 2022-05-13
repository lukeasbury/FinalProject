from tkinter import *
import random


class GUI:
    """
    Class to represent the GUI for the game of rock, paper, scissors
    """
    turns = 0
    comp_points = 0
    player_points = 0

    def __init__(self, window) -> None:
        """
        Method to set up the window and frames for the game
        """
        self.turns: int = GUI.turns
        self.comp_points: int = GUI.comp_points
        self.player_points: int = GUI.player_points

        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Play')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=15)

        self.frame_score = Frame(self.window)
        self.score = Label(self.frame_score, text='Score:')
        self.player = Label(self.frame_score, text=f'Player: {self.player_points}')
        self.computer = Label(self.frame_score, text=f'Computer: {self.comp_points}')
        self.frame_score.pack(padx=5)
        self.frame_score.pack(anchor='w')
        self.score.pack(padx=5, side='left')
        self.player.pack(padx=5, side='left')
        self.computer.pack(padx=5, side='left')

        self.frame_bottom = Frame(self.window)
        self.button_submit = Button(self.frame_bottom, text="Submit", command=self.clicked)
        self.button_submit.pack()
        self.frame_bottom.pack(side='bottom', pady= 10)

    def clicked(self) -> None:
        """
        Method used whenever the submit button is clicked
        -Uses the player input and sets actions accordingly
        -Accounts for score between the player and computer
        -computer is a random descision choice between rock, paper, or scissors
        -Also accounts for exception errors whenever the player does not type rock, paper, or scissor
        """
        game: list = ['rock', 'paper', 'scissor']
        name: str = self.entry_name.get()
        name: str = name.strip().lower()

        try:
            if name not in game:
                raise ValueError
            comp_move = self.comp_move()
            game = self.game(comp_move, name)
            self.label_name.config(padx=100, text=game)

            if 'You win' in game:
                self.turns += 1
                self.player_points += 1
                self.player.config(text=f'Player: {self.player_points}')
            elif 'You lose' in game:
                self.turns += 1
                self.comp_points += 1
                self.computer.config(text=f'Computer: {self.comp_points}')
            else:
                self.turns += 1

            if self.turns == 3 or self.player_points >= 2 or self.comp_points >= 2:
                self.label_name.config(padx=100, text=game)
                self.button_submit.config(text='OK', command=self.game_over)
            else:
                self.button_submit.config(text='OK', command=self.reset)

            self.entry_name.delete(0, END)

        except ValueError:
            self.label_name.config(padx=100, text="Enter Valid Response.")
            self.button_submit.config(text='OK', command=self.reset)

    def reset(self) -> None:
        """
        Method used for whenever the Submit button changes into the OK button
        -The OK button is used to reset the changes made allowing players to input another item
        -Also incorporates the use to reseting player scores whenever the game ends
        """
        self.player.config(text=f'Player: {self.player_points}')
        self.computer.config(text=f'Computer: {self.comp_points}')
        self.entry_name.delete(0, END)
        self.label_name.config(padx=5, text='Play')
        self.button_submit.config(text='Submit', command=self.clicked)

    def comp_move(self) -> str:
        """
        Method utilizing the random function to make a random decision of rock, paper, or scissor
        -As the function name states, this is the computer's move
        """
        return random.choice(["rock", "paper", "scissor"])

    def game(self, comp_move, name) -> str:
        """
        Method representing the actual game
        -Determines whether the player or computer wins, loses, or ties
        """
        if comp_move == "rock" and name == "rock":
            return "Computer is rock. You are rock. You tie."
        elif comp_move == "rock" and name == "paper":
            return "Computer is rock. You are paper. You win."
        elif comp_move == "rock" and name == "scissor":
            return "Computer is rock. You are scissor. You lose."
        elif comp_move == "paper" and name == "rock":
            return "Computer is paper. You are rock. You lose."
        elif comp_move == "paper" and name == "paper":
            return "Computer is paper. You are paper. You tie."
        elif comp_move == "paper" and name == "scissor":
            return "Computer is paper. You are scissor. You win."
        elif comp_move == "scissor" and name == "rock":
            return "Computer is scissor. You are rock. You win."
        elif comp_move == "scissor" and name == "paper":
            return "Computer is scissor. You are paper. You lose."
        elif comp_move == "scissor" and name == "scissor":
            return "Computer is scissor. You are scissor. You tie."

    def game_over(self) -> None:
        """
        Method used for when game ends, determines a winner based off the scores
        -Also is used as a complete reset for the game to start the game over without having to close the program
        """
        if (self.player_points > self.comp_points and self.turns == 3) or self.player_points >= 2:
            self.label_name.config(padx=100, text="GAME OVER - YOU WIN")
        elif (self.comp_points > self.player_points and self.turns == 3) or self.comp_points >= 2:
            self.label_name.config(padx=100, text="GAME OVER - COMPUTER WINS")
        elif (self.comp_points == self.player_points and self.turns == 3):
            self.label_name.config(padx=100, text="GAME OVER - IT'S A TIE")

        self.turns = 0
        self.player_points = 0
        self.comp_points = 0

        self.button_submit.config(text='OK', command=self.reset)
