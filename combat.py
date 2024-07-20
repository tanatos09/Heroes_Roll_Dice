import characters

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def battle(self):
        print(f'The battle between {self.player.name}, and {self.enemy.name}')
        while self.player.is_alive() and self.enemy.is_alive():
            #Player's turn
            self.player.attack(self.enemy)
            if not self.enemy.is_alive:
                print(f'{self.enemy.name} is defeated!')
                break

            self.enemy.attack(self.player)
            if not self.player.is_alive():
                print(f'{self.player.name} is defeated!')
                break

        print('Battle is over')

if __name__ == '__main__':
    player = characters.TestWarrior('Hero', 100, 0, 0,1, 1,0)
    enemy = characters.TestWarrior('Goblin', 100, 0, 0,1, 1,0)
    combat = Combat(player, enemy)
    combat.battle()