import random

def log_action(action):
    def wrapper(*args, **kwargs):
        result = action(*args, **kwargs)
        attacker = args[0]
        target = args[1]
        print(f'{attacker.name} attacks {target.name} for {result} damage')
        return result
    return wrapper

def roll_dice(sides):
    return random.randint(1,sides)

def is_critical(chance=0.2):
    return random.random() < chance
