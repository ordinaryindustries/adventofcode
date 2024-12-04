def load_input():
    with open("input.txt") as f:
        return [line.strip() for line in f]


def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    count = 0

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                match = True
                for k in range(word_len):
                    nr, nc = r + dr * k, c + dc * k
                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or grid[nr][nc] != word[k]
                    ):
                        match = False
                        break
                if match:
                    count += 1

    return count


def main():
    grid = load_input()
    result = count_xmas(grid)
    print(result)


if __name__ == "__main__":
    main()
