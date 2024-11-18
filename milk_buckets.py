# USACO 2024 February Gold 

import sys

n = int(input())
cows = list( map(int, input().split()))

# 1. rotate the list so the smallest element is last
# 2. go backwards through the list, using binary search in insert into the list, making sure
#       That the last element in the list is the last item looped on
# 3. when going backwards, add the item & the shortest stack to another list
# 4. also make an index list

# 5. sum the milk at the start
# 6. go through each cow and its shortest stack, adding a delta milk (-x milk) at the correct index in a tracker list
# 7. go through the tracker list, adding each diff to the sum and printing

milk_sum = sum(cows) #5

def rotate(l, n):
    return l[n:] + l[:n]

class cow:
    def __init__ (self, m, i):
        self.m = m
        self.i = i

cows = rotate(cows, cows.index(min(cows)) + 1)

shortest = [cow(cows[n - 1], n - 1)]
dm = [0] * (n + 1)

for i in range(n - 2, -1, -1):
    cc = cow(cows[i], i)
    if cc.m > shortest[-1].m:
        shortest.append(cc)
    elif cc.m < shortest[-1].m:
        while cc.m < shortest[-1].m :
            shortest.pop()

        shortest.append(cc)
    else:
        shortest[-1].i = i

    current = cows[i]
    si =  i
    for z in range(len(shortest) - 1, -1, -1):
        dm[z.i - si] += shortest[z].m - current
        current = shortest[z].m

for e in range(1, n):
    milk_sum += dm[e]
    sys.stdout.write(str(milk_sum))
    sys.stdout.write('\n')

sys.stdout.write(str(milk_sum))