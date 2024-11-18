f = open("highcard.in", "r")

cn = int(f.readline())
bc = list(range(1, 2 * cn + 1))
ec = []
for _ in range(cn):
	c = int(f.readline())
	ec.append(c)

for i in sorted(ec, reverse=True):
    bc.pop(i - 1)

def binary(v, li):
	t = len(li) - 1
	l = 0
	while (t - l) > 1:
		m = (t + l) // 2
		if v < li[m]:
			t = m
		else: 
			l = m
	if li[l] > v:
		return l 
	return t 

p = 0
for e in ec:
	if e < bc[-1]:
		p += 1
		bc.pop(binary(e, bc))

f = open("highcard.out", "w")
f.write(str(p))