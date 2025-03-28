# jan 2020

f = open("time.in", "r")
input = f.readline

n, m_num, c = map(int,input().split())
m = list(map(int, input().split())) # money earned at city
al = [[] for _ in range(n + 1)] #adj l
for _ in range(m_num):
    a, b = map(int,input().split())
    al[a].append(b)
# dp[state][time]
maxt = max(m) // c + 1
dp = [[-1] * maxt for _ in range(n + 1)] 
dp[1][0] = 0

for t in range(maxt):
    for s in range(1, n + 1):
        if dp[s][t] != -1:
            for ns in al[s]:
                dp[ns][t + 1] = max(dp[ns][t + 1], dp[s][t] + m[ns - 1] - c * (2 * t + 1))

f = open('time.out', "w")
f.write(str(max(dp[1])))