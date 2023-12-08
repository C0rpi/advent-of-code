import re
from functools import reduce
with open("6/input.txt") as f: input = f.read()
def one(input):
    
    rows = [i.group() for i in re.finditer(r"((?=[ ]*)[ \d]+)",input)]
    times = [int(i.group()) for i in re.finditer(r"\d+",rows[0])]
    distances = [int(i.group()) for i in re.finditer(r"\d+",rows[1])]
    
    res = 1
    for run,time in enumerate(times):
        chances = 0
        distance = distances[run]
        d = list()
        for n in range(time):
            # n*time -n**2
            d = (n*(time-n))
            if d>distance:
                chances +=1
        
        if not chances == 0:
            res*=chances
    return res

def two(input):
    
    rows = [i.group() for i in re.finditer(r"((?=[ ]*)[ \d]+)",input)]
    time = int(reduce((lambda a,b: a+b),[(i.group()) for i in re.finditer(r"\d+",rows[0])]))
    distance = int(reduce((lambda a,b: a+b),[(i.group()) for i in re.finditer(r"\d+",rows[1])]))
    res = 0
    mid = time//2
    for n in range(time):#lol
        d = (n*(time-n))
        if d>distance:
            res+=1
    return res
    
print(one(input))
print(two(input))