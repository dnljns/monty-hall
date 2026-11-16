import random

test_trials = 10000
win = "ferrari"
lose = "goat"

def setup_doors():
    doors = [lose, lose, lose]
    doors[random.randint(0, 2)] = win
    return tuple(doors)

def pick_goat(doors, choice):
    choices = [0, 1, 2]
    choices.remove(choice)
    if doors[choice] == win:
        return random.choice(choices)
    else:
        if doors[choices[0]] == win:
            return choices[1]
        else:
            return choices[0]

def game(switch):
    doors = setup_doors()
    choices = [0, 1, 2]
    choice = random.choice(choices)
    goat = pick_goat(doors, choice)
    choices.remove(goat)
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
