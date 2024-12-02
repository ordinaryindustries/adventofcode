from collections import Counter


def load_input():
    with open("input.txt") as f:
        for line in f:
            yield map(int, line.split())


def main():
    left_column = []
    right_column = []

    for left, right in load_input():
        left_column.append(left)
        right_column.append(right)

    right_counts = Counter(right_column)

    return sum(location * right_counts.get(location, 0) for location in left_column)


if __name__ == "__main__":
    print(main())
