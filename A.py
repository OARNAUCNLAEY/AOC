# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
total = 50
cnt = 0
# Print each line
for line in lines:
    move = line.strip()
    rotation = int(move[1:])
    prev_total = total
    cnt += rotation//100
    rotation %= 100
    if move[0] == 'L':
        total -= rotation
        if total <= 0:
            cnt+= (prev_total != 0)
    else:
        total += rotation
        if total >= 100:
            cnt+= (prev_total != 0)
    total %= 100
    total += 100
    total %= 100
print(cnt)
    