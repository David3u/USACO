
n, a, b = map(int,input().split())
v = {}
aj = {}
visited = {}
nodes = set()
for _ in range(n):
    num, id = map(int,input().split())
    v[id] = num 
    aj[id] = []
    visited[id] = False 
    nodes.add(id)

for e in v:
    if a - e in nodes:
        if a - e != e:
            aj[e].append(a - e)
    if a != b:
        if b - e in nodes:
            if b - e != e:
                aj[e].append(b - e)


# all nodes are connected bi-directionally to 0, 1, 2 nodes
# if its 0 connected, we dont care 
# self loops are not optimal, so we process them last
# the rest of the nodes can only form lines 
# cycles cannot exist 
# therefore, we process the node starting at the edges of the lines
# the process the selfloops 
def connect(a, b):
    global pairs
    diff = min(v[a], v[b]) 
    v[a] -= diff 
    v[b] -= diff 
    pairs += diff 

pairs = 0 

#dfs 
for e in visited:
    if visited[e]:
        continue 
    if len(aj[e]) != 1:
        continue 
    
    x = aj[e][0]
    connect(e, x)
    visited[e] = True 
    while True:
        if len(aj[x]) == 1:
            visited[x] = True
            break 
        else:
            visited[x] = True  
            if visited[aj[x][0]]:
                connect(x, aj[x][1])
                x = aj[x][1]
            else:
                connect(x, aj[x][0])
                x = aj[x][0]

# selfpairs 
for e in v:
    if e * 2 == a or e * 2 == b:
        pairs += v[e] // 2

print(pairs)

"""# 2025 open p2

n, a, b = map(int,input().split())
ids = []
for _ in range(n):
    n, d = map(int,input().split())
    ids.append([d, n])

ids.sort() 

# every pairing with a different id is optimal. 
# only self pairing my not be optimal

# therefore, we sort them based on ids
# and use a two pointer from left to right

# start with a goal sum of a, then a goal sum of b. 
# finally, we process id a/2 and id b/2 

pairs = 0
def do(a):
    global pairs
    i = 0 
    j = len(ids) - 1
    while i < j:
        if ids[i][0] + ids[j][0] == a:
            # if they are equal, we pair as much as possible
            diff = min(ids[i][1], ids[j][1])
            pairs += diff 
            ids[i][1] -= diff
            ids[j][1] -= diff  
            i += 1
        elif ids[i][0] + ids[j][0] < a:
            # smaller than a = increase the left pointer 
            i += 1 
        else:
            j -= 1
    if i == j:
        if ids[i][0] * 2 == a:
            return i 
    return -1
ah = do(b)
bh = do(a)
if ah != -1:
    pairs += ids[ah][1] // 2 
if bh != -1:
    pairs += ids[bh][1] // 2 

print(pairs)
"""