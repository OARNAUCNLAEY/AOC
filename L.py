
from tqdm import tqdm
import numpy as np
def parse_input():
    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        puzzle = {}
        i = 0
        queries = []
        while i < len(lines):
            if len(lines[i]) == 1:
                i += 1
                continue
            if "x" in lines[i]:
                grid_size = [int(ch) for ch in lines[i].split(":")[0].split("x")]
                frequency_list = [int(ch) for ch in lines[i].split(":")[1][1:-1].split(" ")]
                queries.append((grid_size, frequency_list))
                i += 1
            else:
                puzzle_ind = int(lines[i].split(":")[0])
                j = i
                while j < len(lines) and len(lines[j]) != 1:
                    j += 1
                grid = []
                for row in range(i + 1, j):
                    cells = lines[row][:-1]
                    temp = []
                    for ch in cells:
                        if ch == '#':
                            temp.append(True)
                        else:
                            temp.append(False)
                    grid.append(np.array(temp))
                puzzle[puzzle_ind] = np.array(grid)
                i = j
            
        return puzzle, queries
def unique_rotations_and_flips(mat):
    """Return a list of unique rotations and flips of the matrix."""
    transformations = []
    # Generate all 8 possible transformations
    for k in range(4):
        rotated = np.rot90(mat, k=k)
        transformations.append(rotated)
        transformations.append(np.fliplr(rotated))
    # Remove duplicates by converting matrices to a hashable type (tuple of tuples)
    unique = []
    seen = set()
    for t in transformations:
        t_tuple = tuple(map(tuple, t))
        if t_tuple not in seen:
            seen.add(t_tuple)
            unique.append(t)
    return unique
def create_puzzle_list(puzzle, frequency):
    puzzle_list = []
    for i in range(len(frequency)):
        for j in range(frequency[i]):
            puzzle_list.append(unique_rotations_and_flips(puzzle[i]))
    return puzzle_list
def can_fill(row, col, puzzle, grid):
    # print(puzzle)
    rows_grid, cols_grid = grid.shape
    rows_puzzle, cols_puzzle = puzzle.shape
    if (row + rows_puzzle > rows_grid) or (col + cols_puzzle > cols_grid):
        return False  # Out of bounds
    
    region = grid[row:row + rows_puzzle, col:col + cols_puzzle]
    overlap = region & puzzle
    if np.any(overlap):
        return False
    return True
def fill_and_clone(row, col, puzzle, grid):
    grid_new = grid.copy()
    rows_grid, cols_grid = grid.shape
    rows_puzzle, cols_puzzle = puzzle.shape
    
    grid_new[row:row + rows_puzzle, col:col + cols_puzzle] = puzzle
    return grid_new
dp = {}
def recur(ind, grid, puzzle_list):
    global dp
    if ind == len(puzzle_list):
        # print(grid)
        return True
    rows, cols = np.where(grid == 0)
    key = tuple(map(tuple, grid))
    if key in dp:
        return dp[key]
    is_possible = False
    for row, col in zip(rows, cols):
        for puzzle in puzzle_list[ind]:
            if can_fill(row, col, puzzle, grid):
                grid_new = fill_and_clone(row, col, puzzle, grid)
                is_possible |= recur(ind + 1, grid_new, puzzle_list)
                if is_possible:
                    break
        if is_possible:
            break
    dp[key] = is_possible
    return is_possible
    
import concurrent.futures
def try_to_fill(grid, puzzle_list):
    global dp
    dp = {}
    return recur(0, grid, puzzle_list)
import multiprocessing

def worker(arg, timeout_sec):
     
    # print(args)
    with multiprocessing.Pool(1) as pool:
        res = pool.apply_async(try_to_fill, (arg,))
        try:
            return res.get(timeout=timeout_sec)
        except multiprocessing.TimeoutError:
            return 0  # or 1, as you prefer
import random
def main_1():
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        global dp
        puzzle, queries = parse_input()
        ans = 0
        # print(queries)
        inputs = []
        cnt = 0
        for query in tqdm(queries):
            grid = np.zeros(query[0]) != 0
            if query[0][0]*query[0][1]/9 -  sum(query[1]) > 0:
                ans += 1
            elif query[0][0]*query[0][1] - query[1][0]*7 - query[1][1]*7 - query[1][2]*7 - query[1][3]*7 - query[1][4]*6 - query[1][5]*5 < 0:
                continue
            else:
                cnt += 1
                puzzle_list = create_puzzle_list(puzzle, query[1])
                random.shuffle(puzzle_list)
                input = (grid, puzzle_list)
                inputs.append(input)
        pool = multiprocessing.Pool()
        async_results = [
            pool.apply_async(try_to_fill, args)
            for args in inputs
        ]
        timeout = 10
        results = []
        for res in tqdm(async_results):
            try:
                results.append(res.get(timeout=timeout))
            except multiprocessing.TimeoutError:
                results.append(0)  # Or 1
        print(sum(results))
        print(ans + sum(results))
        
def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        global dp
        puzzle, queries = parse_input()
        ans = 0
        # print(queries)
        inputs = []
        for query in tqdm(queries):
            grid = np.zeros(query[0]) != 0
            # print(query[0])
            puzzle_list = create_puzzle_list(puzzle, query[1])
            random.shuffle(puzzle_list)
            input = (grid, puzzle_list)
            inputs.append(input)
        pool = multiprocessing.Pool()
        async_results = [
            pool.apply_async(try_to_fill, args)
            for args in inputs
        ]
        timeout = 10
        results = []
        for res in tqdm(async_results):
            try:
                results.append(res.get(timeout=timeout))
            except multiprocessing.TimeoutError:
                results.append(0)  # Or 1
        print(sum(results))
    
        
if __name__ == "__main__":
    main_1()

                
                
                
                
