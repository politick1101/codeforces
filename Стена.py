n, m = map(int, input().split())
for i in range(n):
    s = input()

s = s.strip('.')

while '..' in s:
    s = s.replace('..', '.')

print(len(s.split('.')))
