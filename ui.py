import characters
import dice
from combat import Combat
from gui import BattleGUI


class BattleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battle Simulator")

        self.player = characters.TestWarrior('Hero', 100, 0, 0, 1, 1, 0)
        self.enemy = characters.TestWarrior('Goblin', 100, 0, 0, 1, 1, 0)

        self.dice_options = {'D6': dice.D6, 'D10': dice.D10, 'D12': dice.D12, 'D20': dice.D20, 'D100': dice.D100}
        self.player.attack_dice = self.dice_options['D10']()
        self.enemy.attack_dice = self.dice_options['D6']()

        self.combat = Combat(self.player, self.enemy)
        self.gui = BattleGUI(self.root, self.dice_options, self.player_attack)

        self.update_labels()

    def player_attack(self):
        chosen_dice = self.gui.dice_choice.get()
        self.player.attack_dice = self.dice_options[chosen_dice]()

        self.gui.log_message("Player's turn:\n")

        damage = self.combat.attack(self.player, self.enemy)
        self.update_labels()
        self.log_attack(self.player, self.enemy, damage)

        if not self.enemy.is_alive():
            self.gui.log_message(f'{self.enemy.name} is defeated!\n')
            self.gui.disable_attack_button()
            return

        self.gui.log_message("Enemy's turn:\n")

        damage = self.combat.attack(self.enemy, self.player)
        self.update_labels()
        self.log_attack(self.enemy, self.player, damage)

        if not self.player.is_alive():
            self.gui.log_message(f'{self.player.name} is defeated!\n')
            self.gui.disable_attack_button()

    def update_labels(self):
        self.gui.update_labels(f'Player: {self.player.name} HP: {self.player.health}',
                               f'Enemy: {self.enemy.name} HP: {self.enemy.health}')

    def log_attack(self, attacker, target, damage):
        self.gui.log_message(f'{attacker.name} attacks {target.name} for {damage} damage\n')


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    app = BattleUI(root)
    root.mainloop()
