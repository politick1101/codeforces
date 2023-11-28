# 4
# 4 1
# 2 0
# 12 10
# 14 11
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    for i in range(1, n + 1, 2):
        a, b = i, i + 1

        if (a + k) * b % 4 == 0:
            if i == 1:
                print("YES")
            print(a, b)
            # Проверка
            # print(friends"({a} + {k}) * {b} = {(a + k) * b}")

        elif (b + k) * a % 4 == 0:
            if i == 1:
                print("YES")
            print(b, a)
            # Проверка
            # print(friends"({b} + {k}) * {a} = {(b + k) * a}")

        else:
            print("NO")
            break
