from random import shuffle

n = int(input())

numbers = list(map(str, range(1, n ** 2 + 1)))
shuffle(numbers)

for i in range(n):
    print(" ".join(numbers[i * n: (i + 1) * n]))

shuffle(numbers)
print(" ".join(numbers))
