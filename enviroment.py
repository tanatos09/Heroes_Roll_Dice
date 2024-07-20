import random

#define the base map
class BaseMap:
    def __init__(self, name, description):
        '''

        :param name: name of the map
        :param description: description of the map
        '''
        self.name = name #set the name of the map
        self.description = description #set the description of the map
        self.locations = []#empty list for locations

    def add_location(self, location):
        '''

        :param location: location adding to ghe map
        '''
        self.locations.append(location) #add the location

    def __str__(self):
        '''

        :return: string of the map and location
        '''
        locations_str = '\n'.join(str(loc) for loc in  self.locations)
        return f'{self.name}: {self.description}\nLocations: {locations_str}'

class Location:
    def __init__(self, name, description):
        '''

        :param name: name of the location
        :param description: description of the location
        '''
        self.name = name #set name of the location
        self.description = description #set description of the location
        self.enemies = [] #empty list for enemies

    def add_enemy(self, enemy):
        '''

        :param enemy: adds enemies to the location
        '''
        self.enemies.append(enemy) #add enemy

    def __str__(self):
        '''

        :return: string of enemies in location
        '''
        enemies_str = ', '.join(str(enemy) for enemy in self.enemies)
        return f'Location: {self.name}, {self.description}, Enemies: [{enemies_str}]'
        
class Enemy:
    def __init__(self, name, health):
        '''

        :param name: name of enemy
        :param health: health points of the enemy
        '''
        self.name = name #set name of the enemy
        self.health = health #set health points of the enemy

    def __str__(self):
        '''

        :return: a string of enemy
        '''
        return f'{self.name}, (Health: {self.health})'

#initialize the test map with name and description
class TestMap(BaseMap):
    def __init__(self):
        super().__init__('Test Map', 'Map for testing, with three locations.')
        self.initialize_map() #initialize the map

#create and add locations and enemies on the test map
    def initialize_map(self):
        loc1 = Location('Forest', 'Magic and dark forest.') #set name and description
        loc2 = Location('Rock', 'A rock in a magical forest')
        loc3 = Location('Footpath','Footpath at the end of the magical forest')

        loc1.add_enemy(Enemy('Wolf', 10)) #set name and health points
        loc2.add_enemy(Enemy('Deserter', 10))
        loc3.add_enemy(Enemy('Thief', 10))

#add locations to the map
        self.add_location(loc1)
        self.add_location(loc2)
        self.add_location(loc3)

if __name__ == '__main__':
    test_map = TestMap()
    print(test_map)
