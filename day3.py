def part1(data):
    data = [x.split(")")[0] for x in data.split("mul(") if len(x.split(")")) > 1]
    result = 0
    for x in data:
        x = x.split(",")
        if len(x) != 2:
            continue
        if len(x[0]) > 3 or len(x[1]) > 3:
            continue
        if not (x[0].isdigit() and x[1].isdigit()):
            continue
        num1 = int(x[0])
        num2 = int(x[1])
        result += num1*num2
    return result

def part2(data):
    result = 0
    do_split = data.split("do()")
    working_list = []
    for x in do_split:
        working_list.append(x.split("don't()")[0])
    result = part1("".join(working_list))
    return result

input = ""
with open("inputs/input3.txt", "r") as file:
    for line in file:
        input += line.strip()

print(f"Result 1: {part1(input)}")
print(f"Result 2: {part2(input)}")

