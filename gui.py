import tkinter as tk
from tkinter import ttk

class BattleGUI:
    def __init__(self, root, dice_options, attack_callback):
        self.root = root
        self.dice_options = dice_options
        self.attack_callback = attack_callback

        self.create_widgets()

    def create_widgets(self):
        self.player_label = ttk.Label(self.root, text='Player: HP:')
        self.player_label.grid(row=0, column=0, padx=10, pady=10)

        self.enemy_label = ttk.Label(self.root, text='Enemy: HP:')
        self.enemy_label.grid(row=0, column=1, padx=10, pady=10)

        self.battle_log = tk.Text(self.root, width=50, height=15, state='disabled')
        self.battle_log.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.dice_label = ttk.Label(self.root, text="Choose Dice for Attack:")
        self.dice_label.grid(row=2, column=0, padx=10, pady=10)

        self.dice_choice = ttk.Combobox(self.root, values=list(self.dice_options.keys()))
        self.dice_choice.grid(row=2, column=1, padx=10, pady=10)
        self.dice_choice.current(0)

        self.attack_button = ttk.Button(self.root, text="Attack", command=self.attack_callback)
        self.attack_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def update_labels(self, player_text, enemy_text):
        self.player_label.config(text=player_text)
        self.enemy_label.config(text=enemy_text)

    def log_message(self, message):
        self.battle_log.config(state='normal')
        self.battle_log.insert('end', message)
        self.battle_log.config(state='disabled')
        self.battle_log.see('end')

    def disable_attack_button(self):
        self.attack_button.config(state='disabled')
