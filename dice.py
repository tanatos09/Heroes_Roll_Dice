import random

#define the base class for dice
class Dice:
    def __init__(self, sides=6):
        '''
        :param sides: number of sides of dice, default is 6
        '''
        self.sides = sides # set the number of sides

    def roll(self):
        '''
        :return:  a random number between 1 and the number of sides
        '''
        return random.randint(1, self.sides)

    def multi_roll(self, times):
        '''

        :param times: number of dice rolls
        :return: a list of dice roll values
        '''
        return [self.roll() for _ in range(times)]

    def result_text(self, result):
        '''

        :param result: result of the dice roll
        :return: text of the result
        '''
        return f'You rolled the dice for: {result}'

#define 6-sided dice
class D6(Dice):
    def __init__(self):
        super().__init__(sides=6) #6 sides

class D10(Dice):
    def __init__(self):
        super().__init__(sides=10) #10 sides

class D12(Dice):
    def __init__(self):
        super().__init__(sides=12) #12 sides

class D20(Dice):
    def __init__(self):
        super().__init__(sides=20) #20 sides

class D100(Dice):
    def __init__(self):
        super().__init__(sides=100) #100 sides

class MagicDice(Dice):
    def __init__(self, attacks):
        '''

        :param attacks: list of magics
        '''
        self.attacks = attacks

    def roll(self):
        '''
        select magic
        :return: a random magic
        '''
        return random.choice(self.attacks)

    def result_text(self, result):
        '''

        :param result: selected magic
        :return: text of the selected special attack
        '''
        return f'Your magic dice roll: {result}'


if __name__ == '__main__':
    d6 = D6()
    d10 = D10()
    d12 = D12()
    d20 = D20()
    d100 = D100()
    magic = ['Shield', 'Heal', 'Instant Kill', 'None']
    magic_dice = MagicDice(magic)

    print(d6.result_text(d6.roll()))
    print(d10.result_text(d10.roll()))
    print(d12.result_text(d12.roll()))
    print(d20.result_text(d20.roll()))
    print(d100.result_text(d100.roll()))
    print(f'Your roll of three D10 dice: {d10.multi_roll(3)}')
    use_magic_result = magic_dice.roll()
    print(magic_dice.result_text(use_magic_result))

