import tkinter as tk
from gui import GameGUI
import characters
from ui import GameUI


def main():
    player = characters.TestWarrior('Hero', 100, 0, 0, 1, 1, 0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0, 1, 1, 0)

    game_ui = GameUI(player, enemy)

    root = tk.Tk()

    game_gui = GameGUI(root, game_ui)

    root.mainloop()


if __name__ == "__main__":
    main()
