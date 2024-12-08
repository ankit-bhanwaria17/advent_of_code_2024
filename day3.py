data_list = []
with open("inputs/input3.txt", "r") as file:
    for line in file:
        data_list.append(line)
data = ""    
for x in data_list:
    data += x

print(data)

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
print(result)

