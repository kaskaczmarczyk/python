import sys
signs = ('+', '-', '*', '/')


def calculate():
    a = input("Enter a number (or a letter to exit): ")
    if a.isdigit():
        a = int(a)
    elif a.isalpha():
        sys.exit()

    sign = input("Enter an operation: ")
    while sign not in signs:
        break

    b = input("Enter another number: ")
    if b.isdigit():
        b = int(b)


    if sign == "+":
        print(('{} {}'.format('Result: ', a + b)) + "\n")
    elif sign == "-":
        print(('{} {}'.format('Result ', a - b)) + "\n")
    elif sign == "*":
        print(('{} {}'.format('Result: ', a*b)) + "\n")
    elif sign == "/":
        if b != 0:
            print(('{} {}'.format('Result: ', a/b)) + "\n")
        else:
            print(("Can not be divided by zero.") + "\n")
    else:
        print(("Enter correct sign.") + "\n")


while True:
    calculate()