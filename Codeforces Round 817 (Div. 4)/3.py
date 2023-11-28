for _ in range(int(input())):
    n = int(input())
    friends = []
    scores = [0, 0, 0]
    collection = set()
    for i in range(3):
        words = set(input().split())
        friends.append(words)
        collection.update(words)
    for word in collection:
        finds = [word in friends[i] for i in range(3)]
        count = sum(finds)
        if count == 2:
            points = 1
        elif count == 1:
            points = 3
        else:
            continue
        for i in range(3):
            if finds[i]:
                scores[i] += points
    print(" ".join(map(str, scores)))
