f = open("homework.in", "r")


cases = int(f.readline())


hw = list(map(int, f.readline().split()))

s = 0
m = hw[0]
b = 0
outputs = []
for i in range(1, cases + 1):
	c = hw.pop(-1)
	if c < m:
		m = c 
	s += c 
	if i > 2:
		a = (s - m)/(i - 1)
		if a > b:
			outputs = [cases - i]
			b = a
		elif a == b:
			outputs.append(cases - i)

f = open("homework.out", "w")
f.write("\n".join(map(str, outputs)))