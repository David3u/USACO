# 2025 open p3

# as we build tree, create a prefixsum of enjoyment for each node
# o(n)

# we can use dp to solve this problem
# dp[node][courage] = min_threshold 
# dp[node][courage] = min( 
#   max(dp[node-parent][courage], node_to_parent_skill),
#   dp[node-parent][courage - 1]  )
# o(n * 11)

# then we create a new list
# n[courage] = sorted by thereshold (threshold, enjoyment)
# another list
# m[courage] = same order as n | max enjoyment of this and under
# o (11 * nlogn) 

# for each query:
# for c 0 - courage:
#   m[c][binary_search(n, skill)]
# o(q * 11 * logn)

import bisect

lift_num = int(input())

# enjoyment psum
le = [0]
# lift parents
lp = [0]
# node to parent skill
ns = [0]

for _ in range(lift_num - 1):
    p, d, e = map(int,input().split())
    p -= 1
    le.append(le[p] + e)
    lp.append(p)
    ns.append(d) 
# task 2
dp = [[10000000000] * 11 for _ in range(lift_num)]
dp[0][0] = 0
for i in range(1, lift_num):
    for c in range(11):
        v = 10000000000
        if c != 0:
            if dp[lp[i]][c - 1] != -1:
                v = dp[lp[i]][c - 1]
            v = min(v, dp[i][c - 1])
        if dp[lp[i]][c] != -1:
            v = min(v, max(dp[lp[i]][c], ns[i]))
        dp[i][c] = v 

n = []
for c in range(11):
    cur = []
    for i in range(lift_num):
        cur.append((dp[i][c], le[i]))
    cur.sort() 

    n.append(cur + [])

m = []
for c in range(11):
    cur = []
    current = -1
    for i in range(lift_num):
        current = max(current, n[c][i][1]) 
        cur.append(current)
    m.append(cur + [])

q = int(input())
output = []
for _ in range(q):
    th, c = map(int, input().split())

    thresholds = n[c]
    prefix_max = m[c]

    # Binary search for the largest valid threshold
    idx = bisect.bisect_right(thresholds, (th, float('inf'))) - 1
    if idx < 0:
        output.append(0)
    else:
        output.append(prefix_max[idx])
print("\n".join(map(str, output)))