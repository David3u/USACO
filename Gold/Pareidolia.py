# dp[node][position in bessie] = [cost, # of bessies]
s = input()
c = list(map(int, input().split()))
bessie = "bessie"
dp = [[(0, 30000000000)] * 7 for _ in range(len(c)) ]


def opt(a, b):
    if a[0] > b[0]:
        return a
    if b[0] > a[0]:
        return b
    if a[1] < b[1]:
        return a
    return b

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


dp[0][0] = [0, 0]
for k in range(1, len(s) + 1):
    for j in range(1, 7):
        if s[k - 1] == BESSIE[j - 1]:
            dp[k][j] = opt(add(dp[k - 1][j], (0, c[k - 1])), dp[k - 1][j - 1])
        else:
            dp[k][j] = add(dp[k - 1][j], (0, c[k - 1]))
    dp[k][0] = opt(dp[k - 1][0], add(dp[k][6], (1, 0)))

bessies, cost = dp[len(s)][0]
print(bessies)
print(cost)