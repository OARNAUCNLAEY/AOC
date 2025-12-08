
def valid(i, j, lines):
    return i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0])
with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    ind_s = -1
    total_split = 0
    mark = [['.']*len(lines[0]) for _ in range(len(lines))]
    
    moves =  [[(0, 1), (-1, 1)], [(0, -1), (-1, -1)], [None, (-1, 0)]]
    for i in range(len(lines)):
        if i == 0:
            for j in range(len(lines[0])):
                if lines[i][j] == 'S':
                    ind_s = j
                    mark[i][j] = "|"
        else:
            active_splitters = set()
            for j in range(len(lines[0])):
                flag = False
                for (spliter_check, tachyon) in moves:
                    tachnyon_i = i + tachyon[0]
                    tachnyon_j = j + tachyon[1]
                    if valid(tachnyon_i, tachnyon_j, lines) and mark[tachnyon_i][tachnyon_j] == '|':
                        if spliter_check is not None:
                            spliter_i = i + spliter_check[0]
                            spliter_j = j + spliter_check[1]
                            if valid(spliter_i, spliter_j, lines) and lines[spliter_i][spliter_j] == '^':
                                mark[i][j] = "|"
                                active_splitters.add((spliter_i, spliter_j))
                        elif lines[i][j] != '^':
                            mark[i][j] = "|"
            total_split += len(active_splitters)
    
    
    dp = {}
    def recur(i, j, mark, lines):
        if i == 0:
            if mark[i][j] == '|':
                return 1
            return 0
        ans = 0
        key = (i, j)
        if key in dp:
            return dp[key]
        for (spliter_check, tachyon) in moves:
            tachnyon_i = i + tachyon[0]
            tachnyon_j = j + tachyon[1]
            if valid(tachnyon_i, tachnyon_j, lines) and mark[tachnyon_i][tachnyon_j] == '|':
                if spliter_check is not None:
                    spliter_i = i + spliter_check[0]
                    spliter_j = j + spliter_check[1]
                    if valid(spliter_i, spliter_j, lines) and lines[spliter_i][spliter_j] == '^':
                        ans += recur(tachnyon_i, tachnyon_j, mark, lines)
                elif mark[tachnyon_i][tachnyon_j] == '|':
                     ans += recur(tachnyon_i, tachnyon_j, mark, lines)
        dp[key] = ans
        return ans
    total_timeline = 0
    for j in range(len(lines[0])):
        if mark[len(lines) - 1][j] == '|':
            total_timeline += recur(len(lines) - 1, j, mark, lines)
    for i in range(len(mark)):
        print(''.join(mark[i]))
    print(total_split)
    print(total_timeline)