"""
B. Новая колония
https://codeforces.com/problemset/problem/1481/B
"""

# t = int(input())
n, k = map(int, '13 4'.split())

h = tuple(map(int, '3 3 2 1 3 1 2 4 4 5 4 5 4'.split()))

rocks = []

hole = []

last_height = h[0]

for mt_index, current_height in enumerate(h):
    if current_height > last_height:
        heights = h[mt_index - len(h) - 1::-1]
        max_inner_height = heights[0]
        ln = 0
        for ln, inner_height in enumerate(heights):
            if inner_height > max_inner_height:
                rocks.append((ln, mt_index))
            if inner_height >= current_height:
                break

            max_inner_height = max(inner_height, max_inner_height)

        else:
            rocks.append((ln + 1, mt_index))

    last_height = current_height

print(rocks)
