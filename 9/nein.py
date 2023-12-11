import re

with open("9/input.txt") as f: input = f.readlines()


def one(input):
    res = 0
    for line in input:
        numbers = [int(i.group()) for i in re.finditer(r"[-]?\d+",line)]
        condition = True
        start_numbers = list()
        while condition:
            start_numbers.append(numbers[0])
            differences = list()
            for index,num in enumerate(numbers[:-1]):
                differences.append(numbers[index+1]-num)
            for i in differences:
                if not i == 0:
                    condition = True
                    break
                else:
                    condition = False
            if condition:
                numbers = differences
        numbers.append(numbers[-1])
        index = 0
        start_numbers.pop(-1)
        for s_num in reversed(start_numbers):
            sums = [s_num]
            for num in numbers:
                sum = s_num+num
                sums.append(sum)
                s_num = sum
            numbers = sums
        res+=(sums[-1])
    return res

        
def two(input):
    res = 0
    for line in input:
        numbers = [int(i.group()) for i in re.finditer(r"[-]?\d+",line)]
        condition = True
        start_numbers = list()
        while condition:
            start_numbers.append(numbers[0])
            differences = list()
            for index,num in enumerate(numbers[:-1]):
                differences.append(numbers[index+1]-num)
            for i in differences:
                if not i == 0:
                    condition = True
                    break
                else:
                    condition = False
            if condition:
                numbers = differences
        numbers.append(numbers[-1])
        index = 0
        start_numbers.pop(-1)
        for s_num in reversed(start_numbers):
            first_val = s_num-numbers[0]
            sums = [first_val]
            for num in numbers:
                sum = s_num+num
                sums.append(sum)
                s_num = sum
            numbers = sums
            numbers.insert(0,first_val)#only first value is correct but who cares thats all we need
        res+=(sums[0])
    return res

print(one(input))
print(two(input))