

with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    nodes = []
    for line in lines:
        nodes.append([int(i) for i in line[:-1].split(",")])
    
    pairwise_distance = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            dist = 0
            for k in range(len(nodes[0])):
                dist += (nodes[i][k] - nodes[j][k])**2
            pairwise_distance[i][j] = dist
    flat_pairwise_distance = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            flat_pairwise_distance.append((pairwise_distance[i][j], i, j))
    flat_pairwise_distance.sort()
    parent = [i for i in range(len(nodes))]
    size = [1 for _ in range(len(nodes))]
    def find_parent(u):
        if parent[u] != u:
            parent[u] = find_parent(parent[u])
        return parent[u]
    def merge(u, v):
        pu = find_parent(u)
        pv = find_parent(v)
        if pu != pv:
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
    cnt = 0
    ans = 0
    for dist, u, v in flat_pairwise_distance:
        pu = find_parent(u)
        pv = find_parent(v)
        if u == v:
            continue
        if pu != pv:
            merge(u, v)
            ans = nodes[u][0]*nodes[v][0]
    components = set()
    for i in range(len(nodes)):
        u = find_parent(i)
        components.add((find_parent(i), size[u]))
    components = list(components)
    components.sort(key = lambda x : x[1], reverse = True)
    print(components)
    # print(components[0][1]*components[1][1]*components[2][1])
    print(ans)
            