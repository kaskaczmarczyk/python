def fibonacci(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main(args):
    n = int(input("Podaj nr wyrazu ciągu Fibonacciego: "))
    print(fibonacci(n))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))