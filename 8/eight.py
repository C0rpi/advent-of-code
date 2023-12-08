import re
import math
import copy
with open("8/input.txt") as f: input = f.readlines()

def one(input):
    directions = [i.group() for i in re.finditer(r"[A-Z]",input[0])]
    gowhere = dict()
    for inp in input[2:]:        
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
        
def two(input):
    countlist = [[0,0] for i in range(6)]
    directions = [i.group() for i in re.finditer(r"\w",input[0])]
    gowhere = dict()
    start_nodes = dict()
    for inp in input[2:]:        
        groups = [i.group() for i in re.finditer(r"([A-Z]+)",inp)]
        frm,l,r = (groups[i] for i in range(len(groups)))
        gowhere.update({frm : (l,r)})
        if frm[-1] == 'A':
            start_nodes.update({frm : (l,r)})
    count = 0
    
    while True:
        for i in directions:
            loc_list = dict()
            for _,node in start_nodes.items():
                next_loc = node
                if i == 'R':
                    key = next_loc[1]            
                else: 
                    key = next_loc[0]
                next_loc = gowhere.get(key)
                loc_list.update({key : next_loc})
            start_nodes = loc_list
            count+=1  
            var = True
            #prints difference to last occurence of something that satisfies the end condition
            #"luckily" not alternating
            #solution = lcm(13771, 17873, 23147, 17287, 19631, 20803)
            for v,i in enumerate(loc_list):
                if i[-1] == 'Z':
                    countlist[v][1],countlist[v][0] = countlist[v][0],count
                    print(f"v: {v}, difference: {countlist[v][0] - countlist[v][1]}")
                else:                
                    var = False
            
            if var:
                return 18625484023687 #:)
    """
    fast_list = list()
    for _,node in start_nodes.items():
        next_loc = node
        locs = list()
        condition = True
        locs.append(_)
        last_locs = [i for i in range(1000)]
        while condition:
            for i in directions:
                if i == 'R':
                    key = next_loc[1]            
                else: 
                    key = next_loc[0]
                next_loc = gowhere.get(key)
                locs.append(key)
            if len(set(last_locs)) == len(set(locs)):
                for i in locs:
                    if i[-1] == 'Z':
                        print(i)
                new_locs = list()
                index = locs.index(locs[-1])
                for i in locs:
                    if not i in new_locs:
                        new_locs.append(i)
                    else:
                        break
                condition = False
            last_locs = copy.copy(locs)
        fast_list.append((new_locs,index))
    index_list = list()
    for l in fast_list:
        index_list.append([i for i,v in enumerate(l[0]) if v[-1] =='Z'])
    index_list = list()
    """    

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)        
            
                    
print(one(input))
print(two(input))