import random
from dice import D6, D10, D12, D20, D100, MagicDice

class DiceManager:
    '''
    manages diffrent types of dice rolls
    '''
    def __init__(self):
        '''
        dice types
        '''
        self.dice_types = {
            'D6': D6(),
            'D10': D10(),
            'D12': D12(),
            'D20': D20(),
            'D100': D100()
        }

    def clasic_roll(self,sides):
        '''
        clasic roll with given dice
        :param dice: dice to roll
        :return: random int between 1 and the number of sides
        '''
        return random.randint(1, sides)

    def magic_roll (self, magic_dice):
        '''
        magic roll with given magic dice
        :param magic_dice: magic dice object to roll
        :return: random spell from magic dice
        '''
        return random.choice(magic_dice.spells)

    def multi_roll (self, dice_type, times):
        '''

        perform multiple rolls of the specified dice type
        :param dice_type: select dice (str)
        :param times: how many to roll
        :return: list of dice rolls
        '''
        if dice_type in self.dice_types:
            return [self.clasic_roll(self.dice_types[dice_type].sides) for _ in range(times)]
        else:
            raise ValueError(f'Unsupported dice type: {dice_type}')

    def result_text(self, result):
        return f'Magic roll result {result}'

if __name__ == '__main__':
    warrior_spells = ['Shield', 'Instant kill', 'None', 'None', 'None', 'None', 'None', 'None']
    mage_spells = ['Magic Shield', 'Heal', 'Ice Blast', 'Fireball', 'Lightning storm', 'None', 'None', 'None']

    manager = DiceManager()

    print(manager.clasic_roll(6))
    print(manager.clasic_roll(20))
    print(manager.magic_roll(MagicDice(warrior_spells)))
    print(manager.magic_roll(MagicDice(mage_spells)))
    print(manager.multi_roll('D6', 3))
    print(manager.multi_roll('D100', 10))