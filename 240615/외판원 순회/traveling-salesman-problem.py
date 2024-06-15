import sys
input = sys.stdin.readline
n = int(input())
arr = [[0 for _ in range(n+1)]] + [[0]+list(map(int, input().split())) for _ in range(n)]
# 방문 여부
visited = [False for _ in range(n+1)]

# 지금까지 방문한 지점
combination = []

# 최소 비용
minVal = 1000000
# dfs
def dfs(cnt, before):
    global minVal
    # 모든 지점 다 방문하면 
    if cnt == n:
        # 최소 비용 갱신
        minVal = min(minVal, sum(combination) + arr[before][1])
        return
    for i in range(1, n+1):
        # 방문하지 않았다면 방문
        if not visited[i]:
            # 비용 구함
            val = arr[before][i]
            # 0이 아닐 때만
            if val != 0:
                visited[i] = True
                combination.append(val)
                dfs(cnt+1, i)
                combination.pop()
                visited[i] = False

dfs(0, 1)
print(minVal)