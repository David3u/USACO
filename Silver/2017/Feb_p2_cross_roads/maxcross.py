f = open("maxcross.in", "r")

lights, intv, broken = map(int, f.readline().split())
bl = []
for _ in range(broken):
   bl.append(int(f.readline()))

ll = [0]
for _ in range(lights):
   ll.append(ll[-1])
   if not len(ll) - 1 in bl:
      ll[-1] += 1

best = lights

for i in range(lights - intv + 1):
   broken_num = intv - (ll[i + intv] - ll[i])
   if broken_num < best:
      best = broken_num

f = open("maxcross.out", "w")
f.write(str(best))
f.close()