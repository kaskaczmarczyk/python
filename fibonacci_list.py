"""
    Funkcja zwraca listę liczb ciągu Fibonacciego do n-tego wyrazu.
"""
ciag_fibonacciego = [1, 1]

def fibonacci(n):
    new = 0
    for i in range(1,n-1):
        new = ciag_fibonacciego[-1] + ciag_fibonacciego[-2]
        ciag_fibonacciego.append(new)
    print (ciag_fibonacciego)

def main(args):
    n = int(input("Podaj nr wyrazu ciągu Fibonacciego: "))
    print('Fibonacci sequence:\n')
    fibonacci(n)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
