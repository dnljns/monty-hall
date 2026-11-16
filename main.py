import random

test_trials = 1000000
win = "ferrari"
lose = "goat"
door_count = 3

def setup_doors():
    doors = [lose] * door_count
    doors[random.randint(0, door_count - 1)] = win
    return tuple(doors)

def pick_goats(doors, choice):
    choices = list(range(door_count))
    choices.remove(choice)
    if doors[choice] == win: # Don't show this random door
        choices.remove(random.choice(choices))
    return list([ choice for choice in choices if doors[choice] != win ])

def game(switch):
    doors = setup_doors()
    choices = list(range(door_count))
    choice = random.choice(choices)
    choices = list(set(choices) - set(pick_goats(doors, choice)))
    choices.remove(choice)
    if switch:
        choice = choices[0]
    return doors[choice] == win

if __name__ == "__main__":
    stay_results = []
    for i in range(test_trials):
        stay_results.append(game(False))
    switch_results = []
    for i in range(test_trials):
        switch_results.append(game(True))

    print("Staying win rate:", stay_results.count(True) / len(stay_results) * 100)
    print("Switching win rate:", switch_results.count(True) / len(switch_results) * 100)
