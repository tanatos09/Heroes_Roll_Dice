import random

#define the base class for dice
class Dice:
    def __init__(self, sides=6):
        '''
        :param sides: number of sides of dice, default is 6
        '''
        self.sides = sides # set the number of sides


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

