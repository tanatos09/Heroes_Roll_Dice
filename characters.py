import dice
from utils import roll_dice, is_critical
from dice_manager import DiceManager


class Character():
    def __init__(self, name, health, defense, level, attack_min, attack_max, mana, spells, attack_dice=None, defense_dice=None):
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
        self.dice_manager = DiceManager()
        self.attack_dice = attack_dice if attack_dice else self.d6 #default attack dice D6
        self.defense_dice = defense_dice if defense_dice else self.d6 #default defense dice D6
        self.magic_dice = dice.MagicDice(spells)


    def attack(self, target, clasic_roll):
        '''

        perform an attack on a target

        :param target: target of attack
        :param clasic_roll: dice roll result
        :return: damage dealt to target
        '''
        damage = roll_dice(self.attack_max) + clasic_roll  #calculate base damage

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
        spells = ['Shield', 'Instant kill', 'None', 'None', 'None', 'None', 'None', 'None']
        super().__init__(name, health, defense, level, attack_min, attack_max, mana, spells)



class TestMage(Character):
    def __init__(self, name, health, defense, level, attack_min, attack_max, mana):
        spells = ['Magic Shield', 'Heal', 'Ice Blast', 'Fireball', 'Lighting storm', 'None', 'None', 'None']
        super().__init__(name, health, defense, level, attack_min, attack_max, mana, spells)




if __name__ == '__main__':
    warrior = TestWarrior('Warrior', 100, 5, 1, 5, 10, 20)
    mage = TestMage('Mage', 100, 3, 1, 3, 7, 75)
    target = TestWarrior('TestTarget', 100, 5, 1, 5, 10, 20)

    warrior.attack(target, warrior.dice_manager.clasic_roll(6))
    print(f"{target.name}'s health: {target.health}")

    target.attack(warrior, target.dice_manager.clasic_roll(6))
    print(f"{warrior.name}'s health: {warrior.health}")

    mage.attack(target, mage.dice_manager.clasic_roll(10))
    print(f"{target.name}'s health after attack: {target.health}")

    magic_result = warrior.dice_manager.magic_roll(warrior.magic_dice)
    print('warrior roll magic', warrior.dice_manager.result_text(magic_result))

    magic_result = mage.dice_manager.magic_roll(mage.magic_dice)
    print('mage magic', mage.dice_manager.result_text(magic_result))