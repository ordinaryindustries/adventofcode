from collections import Counter

with open("input.txt") as f:
    left, right = zip(*(map(int, line.split()) for line in f))
    print(sum(x * Counter(right).get(x, 0) for x in left))
