import random, time

test_trials = 10000000
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
    start_total = time.time()
    game_durations = []

    stay_results = []
    for i in range(test_trials):
        start = time.time()
        stay_results.append(game(False))
        game_durations.append(time.time() - start)
    switch_results = []
    for i in range(test_trials):
        start = time.time()
        switch_results.append(game(True))
        game_durations.append(time.time() - start)

    print("Staying win rate:", stay_results.count(True) / len(stay_results) * 100)
    print("Switching win rate:", switch_results.count(True) / len(switch_results) * 100)
    print("Average game duration:", sum(game_durations) / len(game_durations))
    print("Total simulation duration:", time.time() - start_total)
