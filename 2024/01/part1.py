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

    left_column.sort()
    right_column.sort()

    return sum(abs(left - right) for left, right in zip(left_column, right_column))


if __name__ == "__main__":
    print(main())
