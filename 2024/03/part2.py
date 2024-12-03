import re


def load_input():
    with open("input.txt") as f:
        return f.read()


def main():
    total = 0
    enabled = True
    data = load_input()
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)")

    for match in pattern.finditer(data):
        instruction = match.group(0)

        if instruction.startswith("mul"):
            if enabled:
                x, y = map(int, match.groups())
                total += x * y
        elif instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False

    print(total)


if __name__ == "__main__":
    main()
