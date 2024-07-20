import tkinter as tk
from tkinter import ttk
from ui import GameUI
import characters
import dice

class GameGUI:
    def __init__(self, root, game_ui):
        self.root = root
        self.root.title("Heroes Roll Dice")
        self.game_ui = game_ui
        self.d6 = dice.D6()
        self.d10 = dice.D10()
        self.last_roll = None

        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        self.map_frame = ttk.LabelFrame(self.root, text="Map", padding="10")
        self.map_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.animation_frame = ttk.LabelFrame(self.root, text="Animation", padding="10")
        self.animation_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.player_stats_frame = ttk.LabelFrame(self.root, text="Player Stats", padding="10")
        self.player_stats_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.enemy_stats_frame = ttk.LabelFrame(self.root, text="Enemy Stats", padding="10")
        self.enemy_stats_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.dice_frame = ttk.LabelFrame(self.root, text="Dice", padding="10")
        self.dice_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.log_frame = ttk.LabelFrame(self.root, text="Log", padding="10")
        self.log_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.player_health_label = ttk.Label(self.player_stats_frame, text="Health: ")
        self.player_health_label.grid(row=0, column=0, sticky="w")

        self.player_health_value = ttk.Label(self.player_stats_frame, text="")
        self.player_health_value.grid(row=0, column=1, sticky="w")

        self.enemy_health_label = ttk.Label(self.enemy_stats_frame, text="Health: ")
        self.enemy_health_label.grid(row=0, column=0, sticky="w")

        self.enemy_health_value = ttk.Label(self.enemy_stats_frame, text="")
        self.enemy_health_value.grid(row=0, column=1, sticky="w")

        self.attack_button = ttk.Button(self.animation_frame, text="Attack", command=self.attack)
        self.attack_button.grid(row=0, column=0, pady=10)
        self.attack_button.state(["disabled"])

        self.roll_d6_button = ttk.Button(self.dice_frame, text="Roll D6", command=self.roll_d6)
        self.roll_d6_button.grid(row=0, column=0, pady=10)

        self.dice_result_label = ttk.Label(self.dice_frame, text="")
        self.dice_result_label.grid(row=1, column=0, columnspan=2)

        self.log_text = tk.Text(self.log_frame, height=10, state='disabled', wrap='word')
        self.log_text.grid(row=0, column=0, sticky="nsew")

        self.log_scrollbar = ttk.Scrollbar(self.log_frame, orient='vertical', command=self.log_text.yview)
        self.log_scrollbar.grid(row=0, column=1, sticky='ns')
        self.log_text['yscrollcommand'] = self.log_scrollbar.set

    def roll_d6(self):
        self.last_roll = self.d6.roll()
        self.dice_result_label.config(text=f"Rolled D6: {self.last_roll}")
        self.log_message(f"Rolled D6: {self.last_roll}")
        self.attack_button.state(["!disabled"])
        self.roll_d6_button.state(["disabled"])

    def attack(self):
        if self.last_roll is None:
            self.log_message("You must roll the dice first!")
            return

        self.log_message("Player attacks!")
        self.game_ui.attack(self.last_roll)
        self.update_stats()
        self.last_roll = None
        self.attack_button.state(["disabled"])
        self.roll_d6_button.state(["!disabled"])

    def update_stats(self):
        stats = self.game_ui.get_stats()
        self.player_health_value.config(text=str(stats['player_health']))
        self.enemy_health_value.config(text=str(stats['enemy_health']))
        if not self.game_ui.enemy.is_alive():
            self.log_message(f"{self.game_ui.enemy.name} is defeated!")
        if not self.game_ui.player.is_alive():
            self.log_message(f"{self.game_ui.player.name} is defeated!")

    def log_message(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state='disabled')
        self.log_text.yview(tk.END)

if __name__ == '__main__':
    player = characters.TestWarrior('Hero', 100, 0, 0, 1, 1, 0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0, 1, 1, 0)
    game_ui = GameUI(player, enemy)

    root = tk.Tk()
    game_gui = GameGUI(root, game_ui)
    root.mainloop()
