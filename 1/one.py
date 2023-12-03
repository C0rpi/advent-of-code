import re

d = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def repl(inp):
    if inp in d:
        return d[inp]
    return inp

def f1(input):
    res = 0
    for i in input:
        i = i.lower()
        occ = re.findall(r"[0-9]",i)
        res+= int(repl(occ[0])+repl(occ[-1]))
    return res
        
def f2(input):
    res = 0
    for i in input:
        i = i.lower()
        occ = re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))",i)
        res+= int(repl(occ[0])+repl(occ[-1]))
    return res
        
with open("1/input.txt") as f: input = f.readlines() 
        
print(f1(input))
print(f2(input))

