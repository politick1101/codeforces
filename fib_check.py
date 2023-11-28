# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# #         # if n not in cache:
# #         #     res = fib(n - 1) + fib(n - 2)
# #         #     cache[n] = res
# #         # return cache[n]
# #
# #
# # cache = dict()
#
# print(fib(int(input())))

# fib = [1, 1]
# n = int(input())
# while len(fib) < n:
#     fib.append(sum(fib[-2:]))
# print(fib[-1])

def fib_recur(n):
    if n in cache:
        return cache[n]
    val = fib_recur(n - 1) + fib_recur(n - 2)
    cache[n] = val
    return val


cache = {1: 1, 2: 1}

print(fib_recur(int(input())))
