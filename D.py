
grid = []
with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    for line in lines:
        grid.append([])
        for ch in line[:-1]:
            grid[-1].append(ch)
def is_valid(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    if grid[i][j] == '@':
        return True
    return False
total_rolls = 0

adjacent_moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
steps = 0
while True:
    new_grid = [row[:] for row in grid]
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cnt = 0
            for move in adjacent_moves:
                ni = i + move[0]
                nj = j + move[1]
                if is_valid(ni, nj, grid):
                    cnt += 1
            if grid[i][j] == '@' and cnt <= 3:
                new_grid[i][j] = 'X'
                ans += 1
    grid = [row[:] for row in new_grid]
    total_rolls += ans
    steps += 1
    print(f"After step {steps}, eliminated {ans} rolls")
    if ans == 0:
        break

# for i in range(len(new_grid)):
#     print(''.join(new_grid[i]))

print(total_rolls)
