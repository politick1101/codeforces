# def count(string):
#     d = dict()
#     for letter in string:
#         if letter in d:
#             d[letter] += 1
#         else:
#             d[letter] = 1
#     return d
#
#
# t = int(input())
# n = int(input())
# second = input()
# dct = count(second)
# for _ in range(t):
#     n1 = int(input())
#     s1 = input()
#     dct1 = count(s1)
#     if dct == dct1:
#         print("YES")
#     else:
#         print("NO")

t = int(input())
name = set("Timur")
for _ in range(t):
    n = int(input())
    s = input()
    if n == 5 and set(s) == name:
        print("YES")
    else:
        print("NO")
