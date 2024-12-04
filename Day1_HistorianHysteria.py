
list_1, list_2 = [], []

with open("input1.txt", "r") as file:
    for line in file:
        values = [int(i) for i in line.strip().split()]
        list_1.append(values[0])
        list_2.append(values[1])
list_1.sort()
list_2.sort()

res = 0
for i in range(len(list_1)):
    diff = abs(list_1[i]-list_2[i])
    res += diff

print(f"Result: {res}")
