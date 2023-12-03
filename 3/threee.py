import re


with open("3/input.txt") as f: input = f.readlines()
def one(input):
    res = 0
    for i,line in enumerate(input):
        if not i == len(input)-1:
            next_line = input[i+1]
            symbol_below = [index.start() for index in re.finditer(r"[^\.\d\n]",next_line)]
        else:
            next_line,symbol_below = None,None
            
        if not i == 0:
            previous_line = input[i-1]
            symbol_above = [index.start() for index in re.finditer(r"[^\.\d\n]",previous_line)]
        else:
            previous_line,symbol_above = None,None
            
        nums_in_row = [j.group() for j in re.finditer(r"\d+(?=[^\d\n\.])|(?<=[^\d\n\.])\d+",line)]
        num_not_adjacent = re.finditer(r"^\d+(?=(\.))|(?<=\.)\d+(?=[\.\n])",line)
        for num in nums_in_row:
            res+=int(num)
        for num in num_not_adjacent:    
            used = False
            val = int(num.group())
            if next_line and not used:
                for s_index in symbol_below:
                    if s_index>=num.start()-1 and s_index<=num.end():
                        res+=val
                        used = True
                        break
            if previous_line and not used:                    
                for s_index in symbol_above:
                    if s_index>=num.start()-1 and s_index<=num.end():
                        res+=val
                        break
    return(res)

print(one(input))#528819