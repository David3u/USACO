f = open("cardgame.in", "r")

cn = int(f.readline())
bc = list(range(1, 2 * cn + 1))
ec1 = []
ec2 = []
ec = []
for _ in range(cn):
	c = int(f.readline())
	if _ < cn / 2:
		ec1.append(c)
	else:
		ec2.append(c)
	ec.append(c)


ec1.sort(reverse=True)
ec2.sort()

for i in sorted(ec, reverse=True):
    bc.pop(i - 1)

p = 0
for e in ec1:
	if e < bc[-1]:
		print(e, bc[-1])
		bc.pop(-1)
		p += 1
bc.reverse()
for e in ec2:
	if e > bc[-1]:
		print(e, bc[-1])
		bc.pop(-1)
		p += 1

f = open("cardgame.out", "w")
f.write(str(p))