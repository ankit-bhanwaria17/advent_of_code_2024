
list_1, list_2 = [], []

with open("input1.txt", "r") as file:
    for line in file:
        values = [int(i) for i in line.strip().split()]
        list_1.append(values[0])
        list_2.append(values[1])
list_1.sort()
list_2.sort()

list2_dict = {}
for i in list_2:
    if i in list2_dict:
        list2_dict[i] += 1
    else:
        list2_dict[i] = 1

res_1 = 0
res_2 = 0
for i in range(len(list_1)):
    diff = abs(list_1[i]-list_2[i])
    res_1 += diff

    if list_1[i] in list2_dict:
        res_2 += list_1[i]*list2_dict[list_1[i]]

print(f"Result 1: {res_1}")
print(f"Result 2: {res_2}")
