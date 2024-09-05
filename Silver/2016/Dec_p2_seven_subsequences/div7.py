f = open("div7.in", "r")


cn = int(f.readline())
cows = []
for _ in range(cn):
	cows.append(int(f.readline()))

l = [0]
longest = 0

for e in cows:
	val = (l[-1] + e) % 7
	l.append(val)
	dist = len(l) - 1 - l.index(val)
	if dist > longest:
		longest = dist


f = open("div7.out", "w")
f.write(str(longest))
f.close()