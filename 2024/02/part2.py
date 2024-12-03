def load_input():
    with open("input.txt") as f:
        for line in f:
            yield map(int, line.split())


def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)

    return increasing or decreasing


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True

    return False


def main():
    reports = load_input()
    return sum(1 for report in reports if is_safe_with_dampener(list(report)))


if __name__ == "__main__":
    print(main())
