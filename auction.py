input()
p = list(map(int, input().split()))
a, b = sorted(p)[-2:]
print(p.index(b) + 1, a)
