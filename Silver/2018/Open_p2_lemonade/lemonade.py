f = open("lemonade.in", "r")

cases = f.readline()
p = list(map(int, f.readline().split()))

p.sort(reverse=True)
l = 0
for i in p:
	if i >= l:
		l += 1

f = open("lemonade.out", "w")
f.write(str(l))