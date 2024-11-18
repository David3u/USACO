f = open("mountains.in", "r")

cases = int(f.readline())
m = []
for _ in range(cases):
	m.append(list(map(int, f.readline().split())))

m.sort(key = lambda x: x[1], reverse=True)

sm = []
def compare(a, b):
	if a[1] - b[1] <= abs(a[0] - b[0]):
		return True
	return False

for e in m:
	good = True
	for i in sm:
		c = compare(i, e)
		if not c:
			good = False
			break
	if good:
		sm.append(e)

f = open("mountains.out", "w")
f.write(str(len(sm)))