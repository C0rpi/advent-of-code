import re
from dataclasses import dataclass

with open("2/input.txt") as f: input = f.readlines() 

@dataclass
class Game:
    id : int
    blue : int
    red : int
    green : int
    
def one(gamelist):
    res = 0
    for i in gamelist:
        if not i.red>12 and not i.green>13 and not i.blue>14:
            res+=i.id
    return(res)

def two(gamelist):
    res = 0
    for i in gamelist:
        power = i.red*i.blue*i.green
        if power == 0:
            breakpoint()
        res+=power
    return res

gamelist = list()
for i in input:
    id = int(re.findall(r"(?<=Game )\d{1,3}",i)[0])
    blue = int(max([int(i) for i in re.findall(r"\d{1,3} (?=blue)",i)]))
    red = int(max([int(i) for i in re.findall(r"\d{1,3} (?=red)",i)]))
    green = int(max([int(i) for i in re.findall(r"\d{1,3} (?=green)",i)]))
    Game(id,blue,red,green)
    gamelist.append(Game(id,blue,red,green))
            
print(one(gamelist))
print(two(gamelist))