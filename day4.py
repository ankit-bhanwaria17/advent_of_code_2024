def countXmas(data):
    if len(data) < 4:
        return 0
    result = 0
    for i in range(len(data)-3):
        substring = data[i:i+4]
        if substring in ("XMAS", "SAMX"):
            result += 1
    return result

def get_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    diagonals = []
    
    # Collect top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diag = []
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                diag.append(grid[i][j])
        if diag:
            diagonals.append("".join(diag))
    
    # Collect top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diag = []
        for i in range(rows):
            j = i - d + cols - 1
            if 0 <= j < cols:
                diag.append(grid[i][j])
        if diag:
            diagonals.append("".join(diag))
    
    return diagonals

def part1(input):
    size = len(input)
    result = 0
    
    # Horizontal count
    h_count = 0
    for i in input:
        h_count += countXmas(i)
    
    # Vertical count
    v_count = 0
    for i in range(size):
        vertical_str = ""
        for j in range(size):
            vertical_str += input[j][i]
        v_count += countXmas(vertical_str)

    # Diagnoal count
    diag_list = get_diagonals(input)
    d_count = 0
    for x in diag_list:
        d_count += countXmas(x)

    print(f"H: {h_count}, V: {v_count}, D: {d_count}")
    result = h_count + v_count + d_count
    return result

def part2():
    result = 0
    return result

input = []
with open("inputs/input4.txt", "r") as file:
    input = [line.strip() for line in file]

print(f"Result 1: {part1(input)}")