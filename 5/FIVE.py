import re 
with open("5/input.txt") as f: input = f.read()

ranges = [i.group().replace("\n"," ") for i in re.finditer(r"(?<=[^\d])([\d \n]+)(?=[^\d])",input) if not i.group() == ' ']
seeds = [int(i.group()) for i in re.finditer(r"\d+",ranges.pop(0))]
for v in (ranges):
    l = list()
    diffs = list()
    n_groups = [i.group() for i in re.finditer(r"([ \n]\d+){3}",v)]
    for n in n_groups:
        num = [int(i.group()) for i in  re.finditer(r"\d+",n)]
        s_st = num[1]
        r = num[2]   
        diffs.append(num[0]-s_st)
        l.append([s_st,r])
    new_seeds = list()
    for seed in seeds:
        used = False
        for i,v in enumerate(l):
            if seed >=v[0] and seed <=v[0]+v[1]:
                used = True
                new_seeds.append(seed+diffs[i])
                break
        if not used:
            new_seeds.append(seed)
    if len(seeds)> len(new_seeds):
        print()
    seeds = new_seeds
print(min(seeds))
                
    
