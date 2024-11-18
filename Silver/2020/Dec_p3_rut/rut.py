

cnum = int(input())

n = []
e = []

for _ in range(cnum):
	d, x, y = input().split()
	if d == "E":
		e.append([int(x), int(y), _])
	else:
		n.append([int(x), int(y), _])

n.sort()
e.sort(key = lambda x: x[1])

blame = {}
blocked = []

for ce in e:
	remove = []
	for cn in n:
		if cn[0] > ce[0] and cn[1] <= ce[1]:
			if cn[0] - ce[0] < ce[1] - cn[1]:
				remove.append(cn)
				blame[cn[2]] = ce[2]
			elif cn[0] - ce[0] > ce[1] - cn[1]:
				blame[ce[2]] = cn[2]
				break 
	for i in remove:
		n.remove(i)

result = [0] * cnum 

def travel(node):
	if node in blame:
		result[blame[node]] += 1
		travel(blame[node])

for e in blame:
	travel(e)

print("\n".join(map(str, result)))