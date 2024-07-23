import random
from dice import D6, D10, D12, D20, D100, MagicDice

class DiceManager:
    def __init__(self):
        self.dice_types = {
            'D6': D6(),
            'D10': D10(),
            'D12': D12(),
            'D20': D20(),
            'D100': D100()
        }

    def clasic_roll(self,dice):
        return random.randint(1, dice.sides)

    def magic_roll (self, magic_dice):
        return random.choice(magic_dice.spells)

    def multi_roll (self, dice_type, times):
        if dice_type in self.dice_types:
            return [self.clasic_roll(self.dice_types[dice_type]) for _ in range(times)]
        else:
            raise ValueError(f'Unsupported dice type: {dice_type}')

if __name__ == '__main__':
    warrior_spells = ['Shield', 'Instant kill', 'None', 'None', 'None', 'None', 'None', 'None']
    mage_spells = ['Magic Shield', 'Heal', 'Ice Blast', 'Fireball', 'Lightning storm', 'None', 'None', 'None']

    manager = DiceManager()

    print(manager.clasic_roll(manager.dice_types['D6']))
    print(manager.clasic_roll(manager.dice_types['D20']))
    print(manager.magic_roll(MagicDice(warrior_spells)))
    print(manager.magic_roll(MagicDice(mage_spells)))
    print(manager.multi_roll('D6', 3))
    print(manager.multi_roll('D100', 10))