import heapq
cases = int(input())

for _ in range(cases):
    job_num = int(input())
    jobs = []
    for i in range(job_num):
        t, s = map(int,input().split())
        jobs.append([s + t, t, s])
    
    jobs.sort()
    done = [] 
    time = 0 
    output = 0
    for e in jobs:
        heapq.heappush(done, 0 - e[2])
        output += 1
        if time > e[1]:
            time += heapq.heappop(done)
            output -= 1 

        time += e[2]

    print(output)