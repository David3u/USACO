nodes = int(input())
potions = list(map(int, input().split()))
import sys
sys.setrecursionlimit(999999999)

al = []
for e in range(nodes + 1):
	al.append([])

for e in range(nodes - 1):
	a, b = map(int, input().split())
	al[a].append(b)
	al[b].append(a)

leaves = [0] * (nodes + 1)
def dfs(node, parent):
	l = 0
	if al[node] == [parent]:
		leaves[node] = 1
		return 1
	for e in al[node]:
		if e != parent:
			l += dfs(e, node)
	leaves[node] = l
	return l


# DFS, passing up # of leaves and # of potions
# potions will always be less than # of leaves 
# keep doing this then return the number of potions at 1
# becaue order doesnt matter at all 


dfs(1, 1)
potions = potions[:leaves[1]]
enp = [0] * (nodes + 1)
for e in potions:
	enp[e] += 1

def dfs2(node, parent):
	p = enp[node]
	for e in al[node]:
		if e != parent:
			p += dfs2(e, node)
	return min(p, leaves[node])

print(dfs2(1,1))