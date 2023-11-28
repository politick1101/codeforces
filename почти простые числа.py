def is_almost_simple(num):
    dividers = 0

    for div in simples:
        if num % div == 0:
            dividers += 1

            if dividers > 2:
                return False

    if dividers < 2:
        return False

    return True


def is_simple(num):
    for divider in simples:
        if num % divider == 0:
            return False
        if divider > num // 2:
            return True
    return True


simples = []
for i in range(2, 1500):
    if is_simple(i):
        simples.append(i)

n = int(input())

count = 0
for i in range(1, n + 1):
    count += is_almost_simple(i)

print(count)
