import characters
import dice

class GameUI:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.d6 = dice.D6()

    def attack(self, roll):
        if roll < 3:  # Assume roll of 1 or 2 means the attack misses
            self.log_message(f"{self.player.name} misses the attack!")
            return

        self.log_message("Player attacks!")
        player_damage = self.player.attack(self.enemy, roll)
        self.update_combat_status()

        if self.enemy.is_alive():
            enemy_roll = self.d6.roll()  # Roll for enemy attack
            enemy_damage = self.enemy.attack(self.player, enemy_roll)
            self.update_combat_status()

    def update_combat_status(self):
        if not self.enemy.is_alive():
            print(f'{self.enemy.name} is defeated!')
        if not self.player.is_alive():
            print(f'{self.player.name} is defeated!')

    def get_stats(self):
        return {'player_health': self.player.health,
                'enemy_health': self.enemy.health
                }

    def log_message(self, message):
        print(message)


if __name__ == '__main__':
    player = characters.TestWarrior('Hero', 100, 0, 0, 1, 1, 0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0, 1, 1, 0)
    ui = GameUI(player, enemy)
    ui.attack(4)
    print(ui.get_stats())
