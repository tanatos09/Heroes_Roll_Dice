import dice
from utils import log_action, roll_dice, is_critical

class TestWarrior:
    def __init__(self, name, health, defense, level, attack_min, attack_max, stamina):
        self.name = name #character name
        self.health = health #character health
        self.defense = defense #character defense
        self.level = level #character level
        self.attack_min = attack_min #minimum attack of the character for attack range
        self.attack_max = attack_max #maximum attack of the character for attack range
        self.stamina = stamina #character stamina
        self.d6 = dice.D6() #instance of the D6 dice
        self.d10 = dice.D10()  # instance of the D10 dice


    @log_action
    def attack(self, target, roll):
        '''

        perform an attack on a target

        :param target: target of attack
        :return:
        '''
        damage = roll_dice(self.attack_max) + roll #calculate base damage

        if is_critical(): #critical hit - 20% chance for test
            damage *= 3
            print('Critical hit!')

        target.defend(damage)
        return damage

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

