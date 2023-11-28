up = int(input())
down = int(input())

pike = up + down + 1

up_path = []
down_path = []

h = 1

while len(up_path) < up or len(down_path) < down:
    if len(up_path) < up:
        up_path.append(h)
        h += 1
    if len(down_path) < down:
        down_path.append(h)
        h += 1

print(*up_path, pike, *down_path[::-1])
