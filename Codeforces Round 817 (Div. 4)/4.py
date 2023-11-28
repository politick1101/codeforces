# def count_max_val(amount):
#     a = amount // 2 + amount % 2
#     b = a + amount // 2 - 1
#     val = ((a + b) / 2) * (b - a + 1) * 2
#     if amount % 2:
#         val += a - 1
#     return int(val)
#
#
# def get_max_val(ln, p):
#     if p < ln // 2:
#         return ln - p - 1
#     return p
#
#
# n = int(input())
# second = input()
# cur_line = [digit if second[digit] == "L" else len(second) - 1 - digit for digit in range(len(second))]
# cur_val = sum(cur_line)
# max_val = count_max_val(n)
# pointer = 0
# for k in range(1, n + 1):
#     if cur_val < max_val:
#         m_val = get_max_val(n, pointer)
#         cur_val += m_val - cur_line[pointer]
#     print(cur_val)
#

def count_line(line, n):
    return sum(i if line[i] == "L" else n - 1 - i for i in range(n))


n = int(input())
line = input()
perfect_line = "R" * (n // 2 + n % 2) + "L" * (n // 2)
cur_val = count_line(line, n)
perfect_val = count_line(perfect_line, n)
pointer = 0
for k in range(1, n + 1):
    if line != perfect_line:
        while pointer < n:
            if line[pointer] != perfect_line[pointer]:
                line = line[:pointer] + perfect_line[pointer] + line[pointer + 1:]
                pointer += 1
                break
            pointer += 1
        cur_val = count_line(line, n)
    print(cur_val)