import characters
import dice
from dice_manager import DiceManager


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.dice_manager =DiceManager()

    def attack(self, attacker, target):
        roll = self.dice_manager.clasic_roll(attacker.attack_dice.sides)
        damage = attacker.attack(target, roll)
        print(f"{attacker.name} attacks' {target.name} with {attacker.attack_dice.__class__.__name__} for {damage} damage")
        return damage

    def battle(self):
        print(f'The battle between {self.player.name}, and {self.enemy.name} has begun')
        while self.player.is_alive() and self.enemy.is_alive():
            #Player's turn
            self.attack(self.player, self.enemy)
            if not self.enemy.is_alive():
                print(f'{self.enemy.name} is defeated!')

            #Enemy's turn
            if self.enemy.is_alive():
                self.attack(self.enemy, self.player)
                if not self.player.is_alive():
                    print(f'{self.player.name} is defeated!')

        print('Battle is over')

if __name__ == '__main__':
    player = characters.TestWarrior('Hero', 100, 0, 0,1, 1,0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0,1, 1,0)

    player.attack_dice = dice.D10()
    enemy.attack_dice = dice.D6()

    combat = Combat(player, enemy)
    result = combat.battle()
    print(result)