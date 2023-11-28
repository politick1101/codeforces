n, m, minimum, maximum = map(int, input().split())

t = list(map(int, input().split()))

if any(map(lambda tmp: not minimum<=tmp<=maximum, t)):
    print('Incorrect')
elif len(t) + 2 - (minimum in t) - (maximum in t) > n:
    print('Incorrect')
else:
    print('Correct')