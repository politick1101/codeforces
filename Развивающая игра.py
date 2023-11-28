n = int(input())
a = list(map(int, input().split()))

max_power = 16
while n - 1 - 2 ** max_power < 0:
    max_power -= 1

for i in range(1, n):
    steps = 0
    for num_index in range(i):
        power = max_power
        times = 0
        step = 2 ** power
        num = a[num_index]
        while num_index < i:
            if num_index + step < n:
                num_index += step
                times += 1
            else:
                power -= 1
                step = 2 ** power
        steps += num * times
    print(steps)
