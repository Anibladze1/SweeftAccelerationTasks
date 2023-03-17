def bomber_man(n, grid):
    r = len(grid)
    c = len(grid[0])
    res = [["O" for j in range(c)] for i in range(r)]
    if n == 1 or n == 0:
        return grid
    elif n % 2 == 0:
        return res
    else:
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "O":
                    res[i][j] = "."
                    if i > 0:
                        res[i - 1][j] = "."
                    if i < r - 1:
                        res[i + 1][j] = "."
                    if j > 0:
                        res[i][j - 1] = "."
                    if j < c - 1:
                        res[i][j + 1] = "."
        if (n - 3) % 4 == 0:
            return res
        else:
            return grid


def main():
    n = 7
    grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']

    result = bomber_man(n, grid)

    for row in result:
        print("".join(row))


if __name__ == '__main__':
    main()
