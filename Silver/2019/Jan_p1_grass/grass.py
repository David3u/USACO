r = open("planting.in", "r")
n = int(r.readline())

aj = []
for _ in range(n):
	aj.append(0)
for _ in range(n - 1):
	a, b = map(int, r.readline().split())
	a -= 1
	b -= 1
	aj[a] += 1
	aj[b] += 1

r = open("planting.out", "w")
r.write(str(max(aj) + 1))