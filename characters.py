import random
from dice import Dice

class TestWarrior:
    def __init__(self, name, health, defense, level, attack_min, attack_max, stamina):
        self.name = name
        self.health = health
        self.defense = defense
        self.level = level
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.stamina = stamina
        self.dice = Dice()

    def attack(self, target):
        damage = random.randint(self.attack_min, self.attack_max) + self.dice.roll()

        if random.random() < 0.2:
            damage *= 3
            print('Critical hit!')

        target.defend(damage)
        print(f'{self.name} attacks {target.name} for {damage} damage.')

    def defend(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


if __name__ == '__main__':
    test_warrior = TestWarrior('Warrior', 100, 0, 0, 1, 10, 0)

    target = TestWarrior('Target', 100, 0, 0, 1, 10, 0)

    test_warrior.attack(target)
    print(f"{target.name}'s health: {target.health}")

    target.attack(test_warrior)
    print(f"{test_warrior.name}'s health {target.health}")

