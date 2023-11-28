t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    for i, j in zip(s1, s2):
        if i != j and set(i + j) != set("GB"):
            print("NO")
            break
    else:
        print("YES")
