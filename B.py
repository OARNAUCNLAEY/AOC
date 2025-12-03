# Open the file in read mode
from bisect import bisect_left, bisect_right
from tqdm import tqdm
total = 50
cnt = 0
# Print each line
invalid_ids = {}
ranges = []
for i in tqdm(range(1, 10**6)):
    cnt = 2
    while len(str(i)*cnt) <= 100:
        invalid_ids[int(str(i)*cnt)] = True
        cnt += 1


invalid_ids = sorted([int(i) for i in list(set(invalid_ids.keys()))])
prefix = [int(invalid_ids[0])]
for i in range(1, len(invalid_ids)):
    prefix.append(prefix[-1] + int(invalid_ids[i]))
sum_invalid = 0

with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    ranges = lines[0].split(",")
    for range in ranges:
        l, r = map(int, range.split("-"))
        ind_left = bisect_left(invalid_ids, l)
        ind_right = bisect_right(invalid_ids, r) - 1
        if ind_left > ind_right:
            continue
        if ind_left == 0:
            sum_invalid += prefix[ind_right]
        else:
            sum_invalid += (prefix[ind_right] - prefix[ind_left-1])
print(sum_invalid)