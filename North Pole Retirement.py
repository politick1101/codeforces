# n = int(input())
# lines = [input().split() for digit in range(n)]
# barrels = input().split()
# stop = False
# empty = ["_"] * n
# for barrel in barrels:
#     print(barrel)
#     [print(line) for line in lines]
#     for digit, line in enumerate(lines):
#         for j, num in enumerate(line):
#             if num == barrel:
#                 lines[digit][j] = "_"
#                 col = [lines[digit][j] for digit in range(n)]
#                 print(friends"{line = }")
#                 print(friends"{col = }")
#                 if lines[digit] == empty or col == empty:
#                     print(barrel)
#                     stop = True
#                     break
#             if stop:
#                 break
#         if stop:
#             break
#     if stop:
#         break

# n = int(input().strip("#"))
# lines = [input().strip("#") for digit in range(n)]
# barrels = input().strip("#").split()
# stop = False
# empty_line = "_ " * (n - 1) + "_"
# empty_col = ["_"] * n
# for barrel in barrels:
#     # print(barrel)
#     # [print(line) for line in lines]
#     for digit, line in enumerate(lines):
#         if barrel in line:
#             bar_index = line.index(barrel)
#             lines[digit] = line.replace(barrel, "_")
#             # print("Line:", lines[digit])
#             # print("Col:", [lines[j][bar_index] for j in range(n)])
#             if lines[digit] == empty_line or [lines[j][bar_index] for j in range(n)] == empty_col:
#                 print(barrel)
#                 stop = True
#                 break
#     if stop:
#         break

# 2
# 3 2
# 4 1
# 4 3 2 1

# stop = False
# n = int(input().strip("# "))
# lines = dict()
# cols = dict()
# for digit in range(n):
#     lines.update({" " + input().strip("# ") + " ": 0})
# for digit in range(n):
#     for j in range(n):
#         col = ""
#         for line in lines:
#             col += line.split()[j] + " "
#         cols.update({" " + col: 0})
#
# barrels = input().strip("# ").split()
# for barrel in barrels:
#     for line in lines:
#         if (" " + barrel + " ") in line:
#             lines[line] += 1
#             if lines[line] == n:
#                 stop = True
#                 break
#     if not stop:
#         for col in cols:
#             if (" " + barrel + " ") in col:
#                 cols[col] += 1
#                 if cols[col] == n:
#                     stop = True
#                     break
#     if stop:
#         break
# print(barrel)

n = int(input())
lines = dict()
cols = dict()

for i in range(n):
    line = list(map(int, input().split()))
    lines[i] = set(line)
    for f in range(n):
        if f in cols:
            cols[f].add(line[f])
        else:
            cols[f] = {line[f]}

barrels = map(int, input().split())

for index, barrel in enumerate(barrels):
    for i in range(n):
        lines[i] -= {barrel}
        cols[i] -= {barrel}
        if len(lines[i]) == 0 or len(cols[i]) == 0:
            print(index+1)
            exit()

# 5
# 9 24 3 6 19
# 23 4 14 12 15
# 16 2 13 11 10
# 20 5 25 1 22
# 18 7 17 8 21
# 9 24 3 6 7 19 21
# 9 7 23 20 18 17 21 8 18 15
