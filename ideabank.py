def ideabank():
    ideabank = []
    k = ideabank.__len__()
    while True:
        if (ideabank.__len__() == 0):
            idea = input('What is your new idea: ')
            ideabank.append(idea)
        else:
            k = 1
            print('\nYour ideabank: ')
            for i in range(ideabank.__len__()):
                print(str(k) + '. ' + ideabank[i])
                k += 1
            idea = input('\nWhat is your new idea: ')
            ideabank.append(idea)

def list():
    k = 1
    print('\nYour ideabank: ')
    for i in range(ideabank.__len__()):
        print(str(k) + '. ' + ideabank[i])
        k += 1


ideabank()
list()