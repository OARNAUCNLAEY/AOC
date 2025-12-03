
def concat(num, b):
    return str(num) + str(b)
def convert_to_int(s):
    if s == "":
        return 0
    return int(s)
def recur(ind, line, moves_done=0, dp = {}):
    if ind >= len(line) or moves_done == 12:
        return ""
    key = (ind, moves_done)
    if key in dp:
        return dp[key]
    ans = max(convert_to_int(concat(line[ind], recur(ind + 1, line, moves_done + 1, dp))), convert_to_int(recur(ind + 1, line, moves_done, dp)))
    dp[key] = ans
    return ans
with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    ans = 0
    for line in lines:
        ans += convert_to_int(recur(0, line[:-1], 0, {}))  
    print(ans)

