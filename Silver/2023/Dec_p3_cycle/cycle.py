# dec 23 p2

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# all unnamed points are matched 
# rotate and flip b to see highest match with a

ua = [True] * n 
for e in a:
	ua[e - 1] = False 
a2 = []
for i in range(n):
	if ua[i]:
		a2.append(i + 1) 

ua = [True] * n 
for e in b:
	ua[e - 1] = False 
b2 = []
for i in range(n):
	if ua[i]:
		b2.append(i + 1) 


c = 0

# use two points for the sorted other points list
p1 = 0
p2 = 0
max_lim = n - k - 1
while True:
	if p1 > max_lim or p2 > max_lim:
		break
	if p1 == max_lim:
		if b2[p2] > a2[p1]:
			break 
		else:
			if b2[p2] == a2[p1]:
				c += 1
				break
			if p2 == max_lim:
				break 
			p2 += 1
	elif p2 == max_lim:
		if a2[p1] > b2[p2]:
			break
		else:
			if b2[p2] == a2[p1]:
				c += 1
				break
			if p1 == max_lim:
				break 
			p1 += 1

	else:
		if a2[p1] == b2[p2]:
			c += 1
			p1 += 1
			p2 += 1
		else:
			if a2[p1] < b2[p2]:
				p1 += 1
			else:
				p2 += 1



ua = [False] * n
for e in a:
	ua[e - 1] = True

ub = [False] * n
for e in b:
	ub[e - 1] = True

for i in range(n):
	ua[i] = ua[i] and ub[i]

ub = [0] * (n + 1)
for i in range(k):
	ub[a[i]] = i 

t = [] 
for i in range(k):
	e = b[i]
	if ua[e-1]:
		d = abs(ub[e] - i)
		t.append(min(d, k - d))

best = 0
seen = {}
counts = []
for e in t:
	if e in seen:
		counts[seen[e]] += 1 
	else:
		seen[e] = len(seen)
		counts.append(1)

if counts != []:
	best = max(counts)

t = [] 
b.reverse()
for i in range(k):
	e = b[i]
	if ua[e-1]:
		d = abs(ub[e] - i)
		t.append(min(d, k - d))

seen = {}
counts = []
for e in t:
	if e in seen:
		counts[seen[e]] += 1 
	else:
		seen[e] = len(seen)
		counts.append(1)


if counts != []:
	best = max(best, max(counts))
print(best + c)