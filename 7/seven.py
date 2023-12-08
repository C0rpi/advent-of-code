import re



with open("7/input.txt") as f: input = f.readlines()
def one(input):
    l = {'M':'A','L': 'K','K': 'Q','J': 'J','I': 'T','H': '9','G': '8','F': '7','E': '6','D': '5','C': '4','B': '3','A': '2'}
    levels = list()
    for index,inp in enumerate(input):
        bid = int([val.group() for val in re.finditer(r" \d+",inp)][0])
        hand = [val.group() for val in re.finditer(r".*(?= )",inp)][0]
        counts = list()
        for k,i in l.items():
            if i in hand:
                counts.append(hand.count(i))
            else:
                counts.append(None)
        for k,v in l.items():
            hand = hand.replace(v,k)
                    
                
                
        if 5 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":6})
        elif 4 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":5})
        elif 3 in counts and 2 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":4})
        elif 3 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":3})
        elif 2 in counts and 2 in counts[counts.index(2)+1:]:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":2})
        elif 2 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":1})
        else:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":0})
    
    sort = sorted(levels,key = lambda d: (d['strength'],d['hand']))
    res = 0
    for i,v in enumerate(sort):
        res += v['bid']*(i+1)
    return res

def two(input):
    l = {'Z':'A','Y': 'K','X': 'Q','W': 'T','V': '9','I': '8','H': '7','G': '6','F': '5','E': '4','D': '3','C': '2','B': 'J'}
    levels = list()
    for index,inp in enumerate(input):
        bid = int([val.group() for val in re.finditer(r" \d+",inp)][0])
        hand = [val.group() for val in re.finditer(r".*(?= )",inp)][0]
        counts = list()
        for k,i in l.items():
            if i in hand:
                counts.append(hand.count(i))
            else:
                counts.append(0)
        
        
        if counts[-1] > 0 and not counts[-1] == 5:
            i = counts.index(max(counts[:-1]))
            counts[i]+=counts[-1]
            counts[-1] = 0
        
        for k,v in l.items():
            hand = hand.replace(v,k)
                    
                
                
        if 5 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":6})
        elif 4 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":5})
        elif 3 in counts and 2 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":4})
        elif 3 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":3})
        elif 2 in counts and 2 in counts[counts.index(2)+1:]:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":2})
        elif 2 in counts:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":1})
        else:
            levels.insert(0,{"hand": hand, "bid":bid,"index":index,"strength":0})
    
    sort = sorted(levels,key = lambda d: (d['strength'],d['hand']))
    res = 0
    for i,v in enumerate(levels):
        for j in levels[i+1:]:
            if v['hand'] == j['hand']:
                print()
    
    for i,v in enumerate(sort):
        res += v['bid']*(i+1)
    return res



print(one(input))
print(two(input))#not lower than 246027665
