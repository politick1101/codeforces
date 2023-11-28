total = int(input().split()[0])
artur = list(map(int, input().split()))
input()
apples = ["2"] * total
for i in artur:
    apples[i - 1] = "1"

print(" ".join(apples))
