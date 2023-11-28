for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    greatest = numbers[-1]
    pointer = n - 1
    while (cur := numbers[pointer]) <= greatest:
        if pointer == 0:
            break
        greatest = cur
        pointer -= 1
    else:
        pointer += 1

    left = numbers[:pointer]
    right = numbers[pointer:]

    set_left = set(left)
    set_right = set(right)

    intersection = set_left.intersection(set_right)
    reps = len(set_left)

    min_index = len(right)
    rev_right = list(reversed(right))
    for num in intersection:
        index = rev_right.index(num)
        if index < min_index:
            min_index = index
    mid = right[:len(right) - min_index]
    reps += len(set(mid)-intersection)

    print(reps)
