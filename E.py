with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    ranges = []
    queries = []
    mode = 1
    for line in lines:
        if line[0] == '\n':
            mode = 0
            continue
        if mode == 1:
            r = line[:-1].split("-")
            ranges.append((int(r[0]), int(r[1])))
        else:
            queries.append(int(line[:-1]))
    
    flat_range = []
    for r in ranges:
        assert r[0] <= r[1]
        flat_range.append((r[0], -1))
        flat_range.append((r[1], 1))
    flat_range.sort(key = lambda x : x[0])
    
    
    left = 0
    seq_active = 0
    ans = 0
    start = -1
    last_counted = -1
    while left < len(flat_range):
        if flat_range[left][1] == -1:
            seq_active += 1
            if seq_active == 1:
                start = flat_range[left][0]
            left += 1
        elif flat_range[left][1] == 1:
            seq_active -= 1
            if seq_active == 0:
                offset = (last_counted != start)
                ans += flat_range[left][0] - start + offset                
                last_counted = flat_range[left][0]
                start = -1
            left += 1
    print(ans)