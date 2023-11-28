n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    first = a * d
    second = c * b
    if first == second:
        print(0)
    elif first == 0 or second == 0 or first % second == 0 or second % first == 0:
        print(1)
    else:
        print(2)