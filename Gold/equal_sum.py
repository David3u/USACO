# equal sum subarrays

# take all the intervals starting at i n
# make a prefix sum n
# sort the psums (with indicies) nlogn
# go through the list, and for each i from min(a, b) to max(a,b)
#    if abs(a-b) < output[i]: output[i] = abs(a - b) n^2
# overall time complexity is n^3 which is fast enough for n < 500

import heapq

num = int(input())
n = list(map(int, input().split()))

output = [-1] * num 
psum = []
for i in range(num):
    ps = 0
    for e in range(i, num):
        ps += n[e]
        psum.append([ps, i, e])
psum.sort()

mins = [[] for _ in range(num)]
ends = [[] for _ in range(num)]

# update min, update, update ends

for i in range(len(psum) - 1):
    diff = psum[i + 1][0] - psum[i][0]
    pts = [psum[i][1], psum[i][2], psum[i + 1][1], psum[i + 1][2]]
    pts.sort()
    mins[pts[0]].append(diff)
    mins[pts[2]].append(diff)
    ends[pts[1]].append(diff)
    ends[pts[3]].append(diff)

lowest = []
popq = []
for i in range(num):
    for e in mins[i]:
        heapq.heappush(lowest, e)
    output[i] = lowest[0]
    for e in ends[i]:
        heapq.heappush(popq, e) 
    while popq and popq[0] == lowest[0]:
        heapq.heappop(popq)
        heapq.heappop(lowest)

print("\n".join(map(str, output)))