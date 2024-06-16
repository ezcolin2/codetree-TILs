import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 방문 여부
rowVisited = [False for _ in range(n)]
colVisited = [False for _ in range(n)]
# 지금까지 선택한 수들
combination = []

# 최소값 중 최대값
res = 0
# dfs
def dfs(cnt):
    global res
    # n개를 모두 뽑으면
    if (cnt == n):
        # 최소값 중 최대값 갱신
        res = max(res, min(combination))
        return
    for i in range(n):
        for j in range(n):
            # row와 col 모두 방문하지 않았다면 방문
            if not rowVisited[i] and not colVisited[j]:
                rowVisited[i] = True
                colVisited[j] = True
                combination.append(arr[i][j])
                dfs(cnt+1)
                combination.pop()
                colVisited[j] = False
                rowVisited[i] = False
dfs(0)
print(res)