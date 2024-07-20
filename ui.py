import characters

class GameUI:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self):
        self.player.attack(self.enemy)
        self.update_combat_status()

        if self.enemy.is_alive():
            self.enemy.attack(self.player)
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

if __name__ == '__main__':
    player = characters.TestWarrior('Hero', 100, 0,0, 1, 1, 0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0, 1, 1, 0)
    ui = GameUI(player, enemy)

    ui.attack()
    print(ui.get_stats())