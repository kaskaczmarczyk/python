from random import randint

attacker = []
defender = []

while True:
    a = int(input('How many units attack: '))
    if a in range(1, 4):
        attacker_throws = a
        break

while True:
    d = int(input('How many units defend: '))
    if d in range(1, 3):
        defender_throws = d
        break

def risk():
    print('\nDice:')
    print('\tAttacker: ', end=""),
    for i in range(attacker_throws):
        n = randint(1, 6)
        attacker.append(n)
    attacker_sorted = sorted(attacker, reverse=True)
    for i in range(attacker_throws):
        print('{pre}{text}'.format(pre='-', text=attacker_sorted[i]), end="")

    print('\n\tDefender: ', end="")
    for i in range(defender_throws):
        n = randint(1, 6)
        defender.append(n)
    defender_sorted = sorted(defender, reverse=True)
    for i in range(defender_throws):
        print('{pre}{text}'.format(pre='-', text=defender_sorted[i]), end="")

    if (attacker_throws < defender_throws):     #ustalenie liczy pojedynków
        number_of_turns = attacker_throws
    else:
        number_of_turns = defender_throws

    attacker_point = 0
    defender_point = 0
    for i in range(1, number_of_turns+1):
        attacker_number = max(attacker)
        defender_number = max(defender)
        if attacker_number > defender_number:
            defender_point += 1
        else:
            attacker_point += 1
        attacker.remove(attacker_number)
        defender.remove(defender_number)

    print('\n\nOutcome:')
    print('\tAttacker: Lost ' + str(attacker_point) + ' units.')
    print('\tDefender: Lost ' + str(defender_point) + ' units.')


risk()