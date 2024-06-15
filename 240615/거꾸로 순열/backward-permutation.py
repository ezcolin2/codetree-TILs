import sys
input = sys.stdin.readline
n = int(input())

# 인덱스에 해당하는 수를 뽑았는디
visited = [False for _ in range(n+1)]

# 지금까지 선택한 수 조합
arr = []

# dfs
def dfs(cnt):
    # 다 뽑았으면 출력
    if cnt == n:
        print(' '.join(map(str, arr)))
    for i in range(n, 0, -1):
        # 방문하지 않았다면 방문
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(cnt+1)
            visited[i] = False
            arr.pop()

dfs(0)