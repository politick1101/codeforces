n = input()
for i in n:
    if int(i) % 2 - 1:
        print("SAD")
        break
else:
    print("HAPPY")