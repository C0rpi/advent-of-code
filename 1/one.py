import re

d = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def repl(inp):
    if inp in d:
        return d[inp]
    return inp
res = 0
with open("1/input.txt") as f: input = f.readlines() 
for i in input:
    i = i.lower()
    occ = re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))",i,)
    res+= int(repl(occ[0])+repl(occ[-1]))
print(res)

