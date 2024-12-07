def is_increasing(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False
    return True

def is_decreasing(nums):
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            return False
    return True

def is_safe(levels):
    result = True
    if is_increasing(levels) or is_decreasing(levels):
        for i in range(len(levels)-1):
            if abs(levels[i] - levels[i+1]) > 3:
                return False
    else:
        result =  False
    return result

def can_be_made_safe(levels):
    result = False
    for i in range(len(levels)):
        modified_nums = levels[:i] + levels[i+1:]
        if is_safe(modified_nums):
            return True
    return result


result_1 = 0
result_2 = 0

with open("input2.txt", "r") as file:
    for line in file:
        levels = [int(x) for x in line.strip().split()]
        if is_safe(levels):
            result_1 += 1
            result_2 += 1
        elif can_be_made_safe(levels):
            result_2 += 1


print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")