# import random
# import timeit
# import numpy as np
#
# n = int(input())
# f = input()
# s = input()
#
# #
# # # n = int(input())
# # start = timeit.default_timer()
# #
#
# first = np.fromstring(f, sep=' ', dtype=int)
# second = np.fromstring(s, sep=' ', dtype=int)
#
# print(np.where(first == second[0])[0][0])
#
# print(np.fromfunction(lambda x: first[np.where(first == second[x])[0][0]], (n,), dtype=int))
#
# # r = [first[second.index(digit)] for digit in first]
#
# # print(*r)
# # print(first)
# # print(second)
#
# # for x in range(n):
# #     print(first[np.where(second == first[x])[0][0]])
#
# # print(np.fromfunction(lambda y, x: first[np.where(second == first[y])[0][0]], shape=(0, n), dtype=np.int64))
# # print(timeit.default_timer() - start)

# n = int(input())
# first = input().split()
# second = input().split()
#
# order = {v: i for i, v in enumerate(second)}
# res = [first[order[v]] for v in first]
#
# print(*res)

import numpy as np
input()
first = np.fromstring(input(), sep=" ", dtype=int)
second = np.fromstring(input(), sep=" ", dtype=int)
res = second[np.argsort(first-1)]
print(*res)

# n = int(input())
#
# first = tuple(map(int, input().split()))
# second = tuple(map(int, input().split()))
#
# res = [0]*n
#
# for i in range(n):
#     res[first[i]-1] = second[i]
#
# print(*res)