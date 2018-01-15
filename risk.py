from random import randint

attacker = []
defender = []
attacker_throws = randint(1,3)        #liczba rzutów kostką atakującego
defender_throws = randint(1,2)        #liczba rzutów kostką obrońcy

def risk():
    for i in range(attacker_throws):
        n = randint(1, 6)
        attacker.append(n)

    for i in range(defender_throws):
        n = randint(1, 6)
        defender.append(n)

    print('{text} {list_of_throws_attacker}'.format(text='Rzuty atakującego', list_of_throws_attacker=sorted(attacker, reverse=True)))
    print('{text} {list_of_throws_defender}'.format(text='Rzuty obrońcy', list_of_throws_defender=sorted(defender, reverse=True)))

    if (attacker_throws < defender_throws):     #ustalenie liczy pojedynków
        number_of_turns = attacker_throws
    else:
        number_of_turns = defender_throws

    for i in range(1, number_of_turns+1):
        attacker_number = max(attacker)
        defender_number = max(defender)
        if attacker_number > defender_number:
            print('{text} {battle_number} {win} {number} {lost}'.format(text='Pojedynek nr', battle_number=i,
                                                 win='zwyciężył atakujący. Wyrzucił', number=attacker_number,
                                                 lost='. Obrońca traci 1 armię.'))
        else:
            print('{text} {battle_number} {win} {number} {lost}'.format(text='Pojedynek nr', battle_number=i,
                                                 win='zwyciężył obrońca. Wyrzucił', number=defender_number,
                                                 lost='. Atakujący traci 1 armię.'))
        attacker.remove(attacker_number)
        defender.remove(defender_number)


risk()