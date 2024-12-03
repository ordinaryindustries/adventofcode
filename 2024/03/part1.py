import re


def main():
    with open("input.txt") as f:
        pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
        print(sum(int(x) * int(y) for x, y in pattern.findall(f.read())))


if __name__ == "__main__":
    main()
