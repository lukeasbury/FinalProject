import pytest
from gui import *
import random

random.seed(10) #scissor, rock, paper

class Test:
    """
    Class representing the pytest
    """
    def setup_method(self):
        """
        Setup method for pytest
        """
        self.gui = GUI(None)

    def teardown_medod(self):
        """
        Teardown method for pytest
        """
        del self.gui

    def test_comp_move(self):
        """
        Test for gui Method comp_move
        """
        assert self.gui.comp_move() == 'scissor'
        assert self.gui.comp_move() == 'rock'
        assert self.gui.comp_move() == 'paper'

    def test_game(self):
        """
        Test for gui Method game()
        """
        assert self.gui.game('rock', 'rock') == "Computer is rock. You are rock. You tie."
        assert self.gui.game('rock', 'paper') == "Computer is rock. You are paper. You win."
        assert self.gui.game('rock', 'scissor') == "Computer is rock. You are scissor. You lose."
        assert self.gui.game('paper', 'rock') == "Computer is paper. You are rock. You lose."
        assert self.gui.game('paper', 'paper') == "Computer is paper. You are paper. You tie."
        assert self.gui.game('paper', 'scissor') == "Computer is paper. You are scissor. You win."
        assert self.gui.game('scissor', 'rock') == "Computer is scissor. You are rock. You win."
        assert self.gui.game('scissor', 'paper') == "Computer is scissor. You are paper. You lose."
        assert self.gui.game('scissor', 'scissor') == "Computer is scissor. You are scissor. You tie."
        
