import random
from dice import Dice

class TestWarrior:
    def __init__(self, name, health, defense, level, attack_min, attack_max, stamina):
        self.name = name #character name
        self.health = health #character health
        self.defense = defense #character defense
        self.level = level #character level
        self.attack_min = attack_min #minimum attack of the character for attack range
        self.attack_max = attack_max #maximum attack of the character for attack range
        self.stamina = stamina #character stamina
        self.dice = Dice() #instance of the dice

    def attack(self, target):
        '''

        perform an attack on a target

        :param target: target of attack
        :return:
        '''
        damage = random.randint(self.attack_min, self.attack_max) + self.dice.roll() #calculate base damage

        if random.random() < 0.2: #critical hit - 20% chance for test
            damage *= 3
            print('Critical hit!')

        target.defend(damage)
        print(f'{self.name} attacks {target.name} for {damage} damage.')

    def defend(self, damage):
        '''

        reduce health point by the amount of damage
        :param damage: the amount of damage
        :return:
        '''
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        '''

        check if character is stil alive

        :return: True - is alive if self.health > 0
        '''

        return self.health > 0


if __name__ == '__main__':
    test_warrior = TestWarrior('Warrior', 100, 0, 0, 1, 10, 0)

    target = TestWarrior('Target', 100, 0, 0, 1, 10, 0)

    test_warrior.attack(target)
    print(f"{target.name}'s health: {target.health}")

    target.attack(test_warrior)
    print(f"{test_warrior.name}'s health: {test_warrior.health}")

