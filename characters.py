import dice
from utils import roll_dice, is_critical


class Character():
    def __init__(self, name, health, defense, level, attack_min, attack_max, mana, magic_abilities):
        self.name = name  #character name
        self.health = health  #character health
        self.defense = defense  #character defense
        self.level = level  #character level
        self.attack_min = attack_min  #minimum attack of the character for attack range
        self.attack_max = attack_max  #maximum attack of the character for attack range
        self.mana = mana  #character mana
        self.d6 = dice.D6()  #instance of the D6 dice
        self.d10 = dice.D10()  # instance of the D10 dice
        self.d12 = dice.D12()  # instance of the D12 dice
        self.d20 = dice.D20()  # instance of the D20 dice
        self.d100 = dice.D100()  # instance of the D100 dice
        self.magic_dice = dice.MagicDice(magic_abilities)  # instance of the MagicDice dice


    def attack(self, target, roll):
        '''

        perform an attack on a target

        :param target: target of attack
        :param roll: dice roll result
        :return: damage dealt to target
        '''
        damage = roll_dice(self.attack_max) + roll  #calculate base damage

        if is_critical():  #critical hit - 20% chance for test
            damage *= 3
            print('Critical hit!')

        target.defend(damage)
        return damage


    def defend(self, damage):
        '''

        reduce health point by the amount of damage
        :param damage: the amount of damage
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

class TestWarrior(Character):
    def __init__(self, name, health, defense, level, attack_min, attack_max, mana):
        '''

        :param name: character name
        :param health: character health
        :param defense: character defense
        :param level: character level
        :param attack_min: character minimum attack
        :param attack_max: character maximimum attack
        :param mana: character mana
        '''
        magic_abilities = ['Shield', 'Instant kill', 'None', 'None', 'None', 'None', 'None', 'None']
        super().__init__(name, health, defense, level, attack_min, attack_max, mana, magic_abilities)



class TestMage(Character):
    def __init__(self, name, health, defense, level, attack_min, attack_max, mana):
        magic_abilities = ['Magic Shield', 'Heal', 'Ice Blast', 'Fireball', 'Lighting storm', 'None', 'None', 'None']
        super().__init__(name, health, defense, level, attack_min, attack_max, mana, magic_abilities)




if __name__ == '__main__':
    warrior = TestWarrior('Warrior', 100, 5, 1, 5, 10, 20)
    mage = TestMage('Mage', 100, 3, 1, 3, 7, 75)
    target = TestWarrior('TestTarget', 100, 5, 1, 5, 10, 20)

    warrior.attack(target, warrior.d6.roll())
    print(f"{target.name}'s health: {target.health}")

    target.attack(warrior, target.d6.roll())
    print(f"{warrior.name}'s health: {warrior.health}")

    mage.attack(target, mage.d10.roll())
    print(f"{target.name}'s health after attack: {target.health}")

    magic_result = warrior.magic_dice.roll()
    print('warrior roll magic', warrior.magic_dice.result_text(magic_result))

    magic_result = mage.magic_dice.roll()
    print('mage magic', mage.magic_dice.result_text(magic_result))