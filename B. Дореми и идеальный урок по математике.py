def nod_rec(a, b):
    dif = abs(a - b)
    if dif in [a, b]:
        return dif
    else:
        return nod_rec(min(a, b), dif)


def handle_data_set(data):
    nods = set()
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            nod = nod_rec(data[i], data[j])
            if nod == 1:
                return data[-1]
            nods.add(nod)
    return data[-1] // min(nods)


for i in range(int(input())):
    input()
    digits = list(map(int, input().split()))
    print(handle_data_set(digits))
