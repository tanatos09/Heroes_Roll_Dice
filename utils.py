def log_action(action):
    def wrapper(*args, **kwargs):
        result = action(*args, **kwargs)
        attacker = args[0]
        target = args[1]
        print(f'{attacker.name} attacks {target.name} for {result} damage')
        return result
    return wrapper
