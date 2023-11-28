input()
steps = 0
for current, goal in zip(input(), input()):
    step = abs(int(current) - int(goal))
    if step > 5:
        step = 10 - step
    steps += step

print(steps)
