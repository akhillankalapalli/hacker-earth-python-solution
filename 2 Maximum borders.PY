def max_border(grid):
    max_border = 0

    for row in grid:
        curr_border = 0
        for cell in row:
            if cell == '#':
                curr_border += 1
                max_border = max(max_border, curr_border)
            else:
                curr_border = 0

    for col in range(len(grid[0])):
        curr_border = 0
        for row in range(len(grid)):
            if grid[row][col] == '#':
                curr_border += 1
                max_border = max(max_border, curr_border)
            else:
                curr_border = 0

    return max_border

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    print(max_border(grid))  