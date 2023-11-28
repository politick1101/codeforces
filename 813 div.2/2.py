# import math
# import itertools
#
# max_sum = 0
# max_perm = None
# n = 7
# perms = list(itertools.permutations(list(range(1, n + 1))))
# for perm in perms:
#     print(perm)
#     summ = 0
#     for digit, item in enumerate(perm, 1):
#         lcm = math.lcm(digit, item)
#         # print(friends"lcm({digit}, {item}) = {lcm}")
#         summ += lcm
#     print(friends"{summ=}")
#     if summ > max_sum:
#         max_sum = summ
#         max_perm = perm
#
# print(max_perm, max_sum)

for i in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        perm = map(lambda num: num + (1 if num % 2 else -1), range(1, n + 1))
        print(*perm)
    else:
        perm = map(lambda num: num + (1 if num % 2 == 0 else -1), range(2, n + 1))
        print(1, *perm)
