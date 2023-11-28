def check():
    for ai, bi in zip(a, b):
        if ai > bi:
            print("NO")
            return

    for i in range(n - 1):
        if b[i] - b[i + 1] > 1:
            print("NO")
            return

    if a[-1] < b[1] and b[-1] - b[0] > 1:
        print("NO")
        return

    print("YES")


for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    check()
