t = int(input())
for _ in range(t):
    n, k, r, c = map(int, input().split())

    shift = r - c
    s = list("." * n)
    s[::k] = "X" * (n // k)
    s = "".join(s)

    s = s[shift:] + s[:shift]

    for i in range(n):
        print(s)
        s = s[-1:] + s[:-1]
