numbers = [-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43]
n = numbers.__len__()
new_numbers = []

for elem in numbers:
    try:
        if int(elem):
            new_numbers.append(elem)
    except TypeError:
        if elem.__class__ == list:
            for ellist in elem:
                new_numbers.insert(n, ellist)
    except ValueError:
        continue
numbers = new_numbers
n = numbers.__len__()


def minimum():
    min = numbers[0]
    for i in range(n):
        if min > numbers[i]:
            min = numbers[i]
    print(min)


def maximum():
    max = numbers[0]
    for i in range(n):
        if max < numbers[i]:
            max = numbers[i]
    print(max)


def average():
    sum = 0
    for elem in numbers:
        sum += elem
    print(sum/n)


command = input("Co chcesz zrobić? min? max? avg? ")
if command == 'min':
    minimum()
elif command == 'max':
    maximum()
elif command == 'avg':
    average()
else:
    print("Wprowadź prawidowe dane!")
