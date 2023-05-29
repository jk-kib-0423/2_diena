augstums = 5

for rinda in range(augstums * 2 - 1):
    if rinda < augstums:
        zvaigznites = rinda + 1
    else:
        zvaigznites = augstums * 2 - rinda - 1

    for _ in range(zvaigznites):
        print("*", end=" ")
    print()