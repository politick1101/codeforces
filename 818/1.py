from math import lcm, gcd

n = int(input())
s = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        print(a, b, end="")
        if lcm(a, b) / gcd(a, b) > 3:
            print("!")
        else:
            s += 1
            print()

print(s)
