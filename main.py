import tkinter as tk
from PIL import Image, ImageTk
from main_window import HangmanWindow
from hangman import Hangman

game = Hangman()
win = HangmanWindow(game)
handler = win.getWindowHandler()
handler.mainloop()
