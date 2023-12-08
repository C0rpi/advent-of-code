import re

with open("8/input.txt") as f: input = f.readlines()

def one(input):
    directions = [i.group() for i in re.finditer(r"\w",input.pop(0))]
    gowhere = dict()
    for inp in input[1:]:        
        groups = [i.group() for i in re.finditer(r"([A-Z]+)",inp)]
        frm,l,r = (groups[i] for i in range(len(groups)))
        gowhere.update({frm : (l,r)})
    next_loc = gowhere.get('AAA')
    count = 0
    while True:
        for i in directions:
            if i == 'R':
                key = next_loc[1]            
            else: 
                key = next_loc[0]
            next_loc = gowhere.get(key)
            count+=1
            if key == 'ZZZ':
                return count
        
            
print(one(input))