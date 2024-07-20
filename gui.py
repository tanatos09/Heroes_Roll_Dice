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

        # Create labels for player stats
        self.player_health_label = ttk.Label(self.player_stats_frame, text="Health: ")
        self.player_health_label.grid(row=0, column=0, sticky="w")

        self.player_health_value = ttk.Label(self.player_stats_frame, text="")
        self.player_health_value.grid(row=0, column=1, sticky="w")

        # Create labels for enemy stats
        self.enemy_health_label = ttk.Label(self.enemy_stats_frame, text="Health: ")
        self.enemy_health_label.grid(row=0, column=0, sticky="w")

        self.enemy_health_value = ttk.Label(self.enemy_stats_frame, text="")
        self.enemy_health_value.grid(row=0, column=1, sticky="w")

        # Create attack button
        self.attack_button = ttk.Button(self.animation_frame, text="Attack", command=self.attack)
        self.attack_button.grid(row=0, column=0, pady=10)

        # Create dice roll buttons and result label
        self.roll_d6_button = ttk.Button(self.dice_frame, text="Roll D6", command=self.roll_d6)
        self.roll_d6_button.grid(row=0, column=0, pady=10)

        self.roll_d10_button = ttk.Button(self.dice_frame, text="Roll D10", command=self.roll_d10)
        self.roll_d10_button.grid(row=0, column=1, pady=10)

        self.dice_result_label = ttk.Label(self.dice_frame, text="")
        self.dice_result_label.grid(row=1, column=0, columnspan=2)

        # Create text box for log
        self.log_text = tk.Text(self.log_frame, height=10, state='disabled', wrap='word')
        self.log_text.grid(row=0, column=0, sticky="nsew")

        # Add scrollbar to log text
        self.log_scrollbar = ttk.Scrollbar(self.log_frame, orient='vertical', command=self.log_text.yview)
        self.log_scrollbar.grid(row=0, column=1, sticky='ns')
        self.log_text['yscrollcommand'] = self.log_scrollbar.set

    def attack(self):
        self.log_message("Player attacks!")
        self.game_ui.attack()
        self.update_stats()

    def roll_d6(self):
        result = self.d6.roll()
        self.dice_result_label.config(text=f"Rolled D6: {result}")
        self.log_message(f"Rolled D6: {result}")

    def roll_d10(self):
        result = self.d10.roll()
        self.dice_result_label.config(text=f"Rolled D10: {result}")
        self.log_message(f"Rolled D10: {result}")

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

