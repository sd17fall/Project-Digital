import pygame
import random
# import sys
from pynput.keyboard import Key, Controller
# from winning import *
keyboard = Controller()

# pygame.init()


def fake_choice():
    """Choose random column"""
    columns = [1, 2, 3, 4]  # hmmm – this looks like it's from Connect 3.
    # is this dead code? Else, it should probably take a parameter that
    # describes the size of the game board.
    chosen_column = random.choice(columns)
    return str(chosen_column)


def fake_keypress(keypress):
    """simulates keypress"""
    keyboard.press(keypress)
    keyboard.release(keypress)


def fake_player(depth, board, my_turn=True):
    """
    concludes every necessary functions for AI
    """
    return fake_keypress(fake_choice())


if __name__ == '__main__':
    fake_player(4, 2)
    print(fake_choice())
    fake_keypress('4')
