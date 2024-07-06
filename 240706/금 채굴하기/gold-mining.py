import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# k를 입력 받아서 이동할 dx, dy를 반환하는 함수
def make_dx_dy(k):
    dx, dy = [], []
    for i in range(-k, k+1):
        distance = k-abs(i)
        for j in range(-distance, distance+1):
            dx.append(i)
            dy.append(j)
    return dx, dy

# arr[x][y]를 방문할 수 있는지
def can_go(x, y):
    return 0<=x<n and 0<=y<n

# 중심점이 [x][y]이고 k가 k인 경우 캘 수 있는 금의 개수
def get_gold(x, y, dx, dy):
    gold_cnt = 0 # 금의 개수
    for i in range(len(dx)):
        nx, ny = x+dx[i], y+dy[i]
        # 갈 수 있고 금이 있다면 
        if (can_go(nx, ny) and arr[nx][ny] == 1):
            gold_cnt += 1
    return gold_cnt

max_gold = 0
# k인 마름모를 기준으로 할 때 손해를 보지 않고 캘 수 있는 가장 많은 금의 개수
def get_gold_without_loss(k):
    global max_gold
    dx, dy = make_dx_dy(k)
    for i in range(n):
        for j in range(n):

            cnt = get_gold(i, j, dx, dy) # 개수 구함

            benefit = cnt * m - (k**2 + (k+1)**2) # 얻은 이득
            # 손해를 보지 않은 경우만 최대 금의 개수 갱신
            if (benefit >= 0):
                max_gold = max(max_gold, cnt)
for k in range(n):
    get_gold_without_loss(k)
print(max_gold)