f = open("triangles.in", "r")

num = int(f.readline())
s = []
for _ in range(num):
	s.append(list(map(int, f.readline().split())))

x = {}
y = {}

for i in s:
	xi = i[0]
	yi = i[1]
	if xi not in x:
		x[xi] = [yi]
	else:
		x[xi].append(yi)
	
	if yi not in y:
		y[yi] = [xi]
	else:
		y[yi].append(xi)
sum = 0

for i in s:
    xi = i[0]
    yi = i[1]
    xs = 0
    ys = 0
    for e in y[yi]:
        xs += abs(e - xi)
    for e in x[xi]:
        ys += abs(e - yi)
    sum += xs * ys

f = open("triangles.out", "w")
f.write(str(sum % 1000000007))