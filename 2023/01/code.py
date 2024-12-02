import sys

sys.path.append('../../../adventofcode')

from utils import load_input


def main():
    problem_input = load_input('input.txt')

    total = 0

    first_number = 0
    last_number = 0

    for line in problem_input:
        for character in line:
            try:
                number = int(character)
            except:
                continue

            
            


if __name__ == "__main__":
    main()