numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)
n = numbers.__len__()
print(n)
i = 1               #iterator

for i in range(1, n):
    j = 0

    for j in range(n-1):

        if numbers[j] > numbers[j+1]:
            numbers[j] > numbers[j+1]
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        j += 1
    i += 1

print(numbers)