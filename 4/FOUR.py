import re

with open("4/input.txt") as f: input = f.readlines()

def one(input):
    res = 0
    for line in input:
        line = line[[i for i in re.finditer(r"^Card *\d*:",line)][0].end():]
        winning = [i.group() for i in re.finditer(r"\d{1,2}(?=([\d ]*\|))",line)]
        seperator = [i.start() for i in re.finditer(r"\|",line)][0]
        tipped = re.findall(r"\d+",line[seperator:])#positive lookbehind has to be fixed length, couldnt be bothered to fix, this works as well
        c=0
        for i,num in enumerate(winning):
            if num in tipped:
                if c ==0:
                    c =1
                else:
                    c*=2
        res+=c
    return res

def two(input):
    num_cards = [1 for i in range(len(input))]
    for index,line in enumerate(input):
        line = line[[i for i in re.finditer(r"^Card *\d*:",line)][0].end():]
        winning = [i.group() for i in re.finditer(r"\d{1,2}(?=([\d ]*\|))",line)]
        seperator = [i.start() for i in re.finditer(r"\|",line)][0]
        tipped = re.findall(r"\d+",line[seperator:])#positive lookbehind has to be fixed length, couldnt be bothered to fix, this works as well
        count=0
        for i,num in enumerate(winning):
            if num in tipped:
                count+=1
        num_cards[index+1:index+1+count] = [i+num_cards[index] for i in num_cards[index+1:index+1+count]]
    
    return sum(num_cards)

print(one(input))#22897
print(two(input))