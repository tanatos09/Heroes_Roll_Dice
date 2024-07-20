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

#define 6-sided dice
class D6(Dice):
    def __init__(self):
        super().__init__(sides=6) #6 sides

if __name__ == '__main__':
    d6 = D6()

    print(f'Rolling a D6: {d6.roll()}')