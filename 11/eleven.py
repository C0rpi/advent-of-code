import re

with open("11/input.txt") as f: input = [i.strip() for i in f.readlines()]


def one(input : list):
    output = input.copy()
    
    n = 0    
    for index, line in enumerate(input):
        if not [i for i in re.finditer(r'[^\.\n]',line)]:
            output.insert(index+n,line)
            n+=1
            
    n = 0
    for index,_ in enumerate(input[0]):
        b = True
        for line in input:
            if not line[index] == '.':
                b = False
                break
        if b:
            n +=1
            for i, line in enumerate(output):
                output[i] = line[:index+n] + '.' + line[index+n:]
        
    i_list = list()
    for index, line in enumerate(output):
        l = [i.start() for i in re.finditer(r'#',line)]
        for i in l:
            i_list.append((index,i))
    distances = list()
    for index, coord in enumerate(i_list):
        for coord2 in i_list[index+1:]:
            distances.append(abs(coord[0]-coord2[0])+abs(coord[1]-coord2[1]))
    return sum(distances)

def two(input):
    output = input.copy()
    
    n = 0    
    for index, line in enumerate(input):
        if not [i for i in re.finditer(r'[^\.\n]',line)]:
            output.insert(index+n,'x'*len(line))
            n+=1
            
    n = 0
    for index,_ in enumerate(input[0]):
        b = True
        for line in input:
            if not line[index] == '.':
                b = False
                break
        if b:
            for i, line in enumerate(output):
                output[i] = line[:index+n] + 'x' + line[index+n:]
            n +=1
        
    i_list = list()
    for index, line in enumerate(output):
        l = [i.start() for i in re.finditer(r'#',line)]
        for i in l:
            i_list.append((index,i))
    distances = list()
    for index, coord in enumerate(i_list):
        for coord2 in i_list[index+1:]:          
            distances.append(abs(coord[0]-coord2[0])+abs(coord[1]-coord2[1]))
            for i in output[coord[0]][min(coord[1],coord2[1]):max(coord[1],coord2[1])+1]:
                if i == 'x':
                    distances[-1]+=1000000-2 #trial and error for -2 
            for l in output[min(coord[0],coord2[0]):max(coord[0],coord2[0])+1]:
                if l[coord[1]] == 'x':
                    distances[-1]+=1000000-2 #why -2?? im confused
                    
    return sum(distances)

print(one(input))#9445168
print(two(input))#742305960572
