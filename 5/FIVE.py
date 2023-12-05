import re 
with open("5/input.txt") as f: input = f.read() + "\n"
def one(input, seeds = None):
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
        seeds = new_seeds
    return min(seeds)

def two(input):
    #this is horrendous by design
    ranges = [i.group().replace("\n"," ") for i in re.finditer(r"(?<=[^\d])([\d \n]+)(?=[^\d])",input) if not i.group() == ' ']
    seeds = [(i[0],i[0]+i[1]) for i in [[int(i.group()) for i in j] for j in [re.finditer(r"\d+",k) for k in [(i.group()) for i in re.finditer(r"([ \n]\d+){2}",ranges.pop(0))]]]]
    for v in ranges:
        nums = [(n[0],n[0]+n[2],n[1],+n[1]+n[2]) for n in [[int(j.group())for j in i] for i in  [re.finditer(r"\d+",n) for n in [i.group() for i in re.finditer(r"([ \n]\d+){3}",v)]]]]
        sources = [(i[2],i[3]) for i in nums]
        diffs = [i[2]-i[0] for i in nums]
        new_seeds = list()
        
        for sindex, source in enumerate(sources):
            for index,seed in enumerate(seeds):
                if seed:
                    if seed[0]>= source[0] and seed[0] < source[1]:
                        
                        if seed[1]>=source[1]:
                            left = (seed[0]-diffs[sindex],source[1]-diffs[sindex])
                            right = (source[1],seed[1])
                            new_seeds.append(left)
                            new_seeds.append(right)
                            seeds[index] = None
                        else:
                            left = (seed[0]-diffs[sindex],seed[1]-diffs[sindex])
                            new_seeds.append(left)
                            seeds[index] = None
                    
                    elif seed[0]<source[0] and seed[1]>=source[0]:
                        if seed[1]>=source[1]:
                            _left = (seed[0],source[0])
                            _middle = (source[0]-diffs[sindex],source[1]-diffs[sindex])
                            _right = (source[1],seed[1])
                            new_seeds.append(_left)
                            new_seeds.append(_middle)
                            new_seeds.append(_right)
                            seeds[index] = None
                        else:
                            left = (seed[0],source[0])
                            right = (source[0]-diffs[sindex],seed[1]-diffs[sindex])
                            new_seeds.append(left)
                            new_seeds.append(right)
                            seeds[index] = None
                            
        [new_seeds.append(seed) for seed in seeds if seed]
        seeds = new_seeds
    return min([seed[0] for seed in seeds])
        
print(one(input))#309796150
print(two(input))#not 15101795 
                    # 50716416