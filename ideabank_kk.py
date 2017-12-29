
def ideabank():
    plik_tekstowy = open("ideabank.txt", mode='a+')
    plik_tekstowy.close()

    plik_tekstowy = open('ideabank.txt', mode='r')
    idea = input('What is your new idea: ')
    l = len(plik_tekstowy.readlines())
    plik_tekstowy.close()
    plik_tekstowy = open('ideabank.txt', mode='a')
    plik_tekstowy.write(idea + '\n')
    plik_tekstowy.close()

    plik_tekstowy = open('ideabank.txt', mode='r')
    if l > 0:
        print('\nYour ideabank: ')
        for indeks, line in enumerate(plik_tekstowy.readlines(), start=1):
            print('{no}. {idea}'.format(no=indeks, idea=line))
    plik_tekstowy.close()

ideabank()


