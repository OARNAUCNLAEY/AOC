
op = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}
with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    row_input = []
    for line in lines:
        row_input.append(line[:-1] + " ")
        print(row_input[-1])
    ops = [tok for tok in row_input[-1].strip().split(" ") if len(tok) > 0]
    row_input = row_input[:-1]
    total_ans = 0
    ind = 0
    for i in range(len(ops)):
        ans = -1
        while(ind < len(row_input[0])):
            
            collect_str = ""
            for j in range(len(row_input)):
                collect_str += row_input[j][ind]
            collect_str = collect_str.strip()
            
            if len(collect_str) == 0:
                ind += 1
                break
            if ans == -1:
                ans = int(collect_str)
            else:
                ans = op[ops[i]](ans, int(collect_str))
            ind += 1
            
        if len(collect_str) == 0:
            total_ans += ans
    print(total_ans)