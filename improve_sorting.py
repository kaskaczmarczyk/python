numbers = []


def input_number():
    table = input("Podaj liczy do posortowania oddzielone tylko spacją: ").split(" ")


    for number in table:
        numbers.append(int(number))
    print(numbers)


def sort_in_numbers():
    for i in range(1, numbers.__len__()):
        veryfication()
        i += 1
    print(numbers)


def veryfication():
    for j in range(numbers.__len__() - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j] > numbers[j + 1]
            temp = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = temp
        j += 1


try:
    input_number()
    sort_in_numbers()
except ValueError:
    print("Błędne dane. Wprowadź liczby.")


