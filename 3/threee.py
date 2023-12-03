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
def two(input):  
    res = 0  
    for i,line1 in enumerate(input):
        if not i == len(input)-1:
            line2 = input[i+1]
            nums_below = [(res.start(),res.end(),res.group())for res in re.finditer(r"\d+",line2)]
        else:
            line2 = None   
            nums_below = None         
        if not i == 0:
            line0 = input[i-1]
            nums_above =[(res.start(),res.end(),res.group())for res in re.finditer(r"\d+",line0)]
        else:
            line0 = None
            nums_above = None
            
            
        stars_in_row = re.finditer(r"\*",line1)
        nums_in_row = [(res.start(),res.end(),res.group())for res in re.finditer(r"\d+(?=[\*])|(?<=[\*])\d+",line1)]
        for star in stars_in_row:
            adj_num = list()
            index = star.start()
            print([nl[2] for nl in nums_above])
            for num in nums_above:
                if (num[0]<=index and num[1]>=index) or (num[0]==index+1):
                    adj_num.append(num[2])
            for num in nums_below:
                if (num[0]<=index and num[1]>=index) or (num[0]==index+1):
                    adj_num.append(num[2])
            for num in nums_in_row:
                if (num[0]<=index and num[1]>=index) or (num[0]==index+1):
                    adj_num.append(num[2])
                    
            if len(adj_num)==2:
                res+=int(adj_num[0])*int(adj_num[1])
            elif len(adj_num)>2:
                print()
    return res
                    
                
            

print(one(input))#528819
print(two(input))#80403602