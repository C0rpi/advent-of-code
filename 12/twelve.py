import re

with open("12/input.txt") as f: input = [i.strip() for i in f.readlines()]


def one(input : list):
    
    def sat_cond(line):
        h = [len(i.group()) for i in re.finditer(r'#+',line)]
        if h == [int(i.group()) for i in re.finditer(r'\d+',line)]:
            return True
        return False
    def iterate_last_char(line, q):
        out = 0
        for i in q:
            new_line = line[:i]+'#' + line[i+1:]
            if sat_cond(new_line): out+=1
        return out        
            
    def split_lines(line, q : list,sum):
        out = 0
        if sum > 1:
            for index, i in enumerate(q):
                new_line = line[:i] + '#' + line[i+1:]
                if sum-1<=1:
                    out = iterate_last_char(new_line,q[index+1:])
                    return out
                else:
                    for i in q[index+1:]:
                        out+=split_lines(new_line,q[index+1:],sum-1)
            return out
        else:
            out = iterate_last_char(line,q)
            return out

    
    out = list()
    for line in input:
        q_index  = [i.start() for i in re.finditer(r'\?',line)]
        h_index  = [i.start() for i in re.finditer(r'#',line)]
        nums  = [int(i.group()) for i in re.finditer(r'\d+',line)]
        leftovers = -len(h_index)+sum(nums)
        
        print(split_lines(line,q_index,sum(nums)-len(h_index)))

def two(input):
    return 

print(one(input))
print(two(input))
