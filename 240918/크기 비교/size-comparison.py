n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j] = 1
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] == 0 and graph[j][i] == 0:
            cnt+=1
    print(cnt)