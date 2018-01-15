doors = [False] * 101

for turn in range(1, 101, 1):

    for i in range(0, len(doors), turn):
        open = doors[i]
        doors[i] = not open

print("Open doors: ", end="")
for i in range(0, len(doors)):
    if doors[i]:
        print(str(i), end=", ")


