f = open("loan.in", "r")

o, d, m = map(int, f.readline().split())

def sim(o, d, m, x):
    paid = 0
    i = 0
    while paid < o:
        c = (o - paid) // x
        if c <= m:
            if paid + m * (d - i) >= o:
                return True
            else:
                return False
        paid += c
        i += 1
        if c * (d - i) + paid < o:
            return False
        if i > d:
            return False 
    return True

v1 = 1
v2 = o
mid = (v1 + v2) // 2
while v1 < v2 - 1:
    if sim(o, d, m, mid):
        v1 = mid 
    else:
        v2 = mid 
    mid = (v1 + v2) // 2

f = open("loan.out", "w")

f.write(str(v1))



