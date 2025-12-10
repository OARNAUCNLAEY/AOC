def is_valid(coord, x, last_y, below_threshold):
    if coord[0] >= x and coord[1] <= last_y and coord[1] >= below_threshold:
        return True
    return False
def calculate_area(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from tqdm import tqdm

def intersect_with_border(cord1, cord2, cords):
    for i in range(len(cords) - 1):
        if cords[i][0] == cords[i + 1][0]:
            x = cords[i][0]
            for y in range(min(cords[i][1], cords[i + 1][1]), max(cords[i][1], cords[i + 1][1]) + 1):
                if x > min(cord1[0], cord2[0]) and x < max(cord1[0], cord2[0]) and y > min(cord1[1], cord2[1]) and y < max(cord1[1], cord2[1]):
                    return True
        else:
            y = cords[i][1]
            for x in range(min(cords[i][0], cords[i + 1][0]), max(cords[i][0], cords[i + 1][0]) + 1):
                if x > min(cord1[0], cord2[0]) and x < max(cord1[0], cord2[0]) and y > min(cord1[1], cord2[1]) and y < max(cord1[1], cord2[1]):
                    return True
    return False

def check_candidate(triple, coords):
    area, i, j = triple
    if not intersect_with_border(coords[i], coords[j], coords):
        return area
    return None

def main():
    answer = []
    coords = []
    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        for line in lines:
            coords.append([int(i) for i in line[:-1].split(",")])
        coords.append(coords[0])
        ans = 0
        for i in tqdm(range(len(coords))):
            for j in range(len(coords)):
                if i == j:
                    break
                    # print(coords[i], coords[j], calculate_area(coords[i], coords[j]))
                answer.append((calculate_area(coords[i], coords[j]), i, j))
    answer.sort(reverse=True)

    func = partial(check_candidate, coords=coords)

    with ProcessPoolExecutor(max_workers=64) as ex:
        for res in tqdm(ex.map(func, answer), total=len(answer)):
            if res is not None:
                ans = max(ans, res)

    print(ans)

if __name__ == "__main__":
    main()

                
                
                
                
