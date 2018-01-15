import sys


def czy_wypisac_imie(args):
    if args.__len__() > 1:
        return True
    else:
        return False


if czy_wypisac_imie(sys.argv):
    print("Hello " + " ".join(sys.argv[1:]))
else:
    print("Hello World!!")



