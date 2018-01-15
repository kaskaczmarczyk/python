import sys
signs = ('+', '-', '*', '/')

def calculate():
    a = input("Enter first number and press 'Enter': ")
    if a.isdigit():
        a = int(a)
    elif a.isalpha():
        sys.exit()

    sign = input("To add press '+', to subtract press '-', to multiply press '*', to divide press  '/' "
                 "and press 'Enter'. ")
    while sign not in signs:
        break

    b = input("Enter second number and press 'Enter': ")
    if b.isdigit():
        b = int(b)
    elif b.isalpha():
        sys.exit()

    if sign == "+":
        print(('{} {}'.format('Addition result: ', a + b)) + "\n")
    elif sign == "-":
        print(('{} {}'.format('Subtraction result: ', a - b)) + "\n")
    elif sign == "*":
        print(('{} {}'.format('Multiplication result: ', a*b)) + "\n")
    elif sign == "/":
        if b != 0:
            print(('{} {}'.format('Division result: ', a/b)) + "\n")
        else:
            print(("Can not be divided by zero.") + "\n")
    else:
        print(("Enter correct sign.") + "\n")


while True:
    calculate()



