for i in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ps = sorted(p)
    minimums = ps[:k]
    print(len(set(p[:k]).difference(set(minimums))))