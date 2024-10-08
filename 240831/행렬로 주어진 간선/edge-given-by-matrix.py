import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][i] = 1
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for row in graph:
    for val in row:
        print(val, end = ' ')
    print()