def ideabank():
    try:
        plik_tekstowy = open("ideabank.txt", mode='a+')
        plik_tekstowy.close()
    except IOError:
        pass

    try:
        plik_tekstowy = open('ideabank.txt', mode='r')
        try:
            idea = input('What is your new idea: ')
            l = len(plik_tekstowy.readlines())
        finally:
            plik_tekstowy.close()
    except IOError:
        pass

    try:
        plik_tekstowy = open('ideabank.txt', mode='a')
        try:
            plik_tekstowy.write(idea + '\n')
        finally:
            plik_tekstowy.close()
    except IOError:
        pass


def lista():
    try:
        plik_tekstowy = open('ideabank.txt', mode='r')
        print('\nYour ideabank: ')
        try:
            for indeks, line in enumerate(plik_tekstowy.readlines(), start=1):
                    print('{no}. {idea}'.format(no=indeks, idea=line))
        finally:
            plik_tekstowy.close()
    except IOError:
        pass

ideabank()
lista()

