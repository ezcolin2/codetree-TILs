import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# 각 턴마다 움직일 말
players = []

# 움직일 말들을 모두 선택한 후 실제로 움직이는 함수
def movePlayer():
    locations = [0 for _ in range(k)] # 각 말들의 현재 위치
    for i in range(n):
        player = players[i] # 움직일 말
        locations[player] += arr[i] # 움직임
    cnt = 0 # 끝까지 도달한 말의 개수
    for location in locations:
        if location>=m-1:
            cnt+=1
    return cnt

res = 0 # 최대로 얻을 수 있는 점수 
# currIdx 턴에 움직일 말을 선택하는 함수
def choosePlayer(currIdx):
    global res
    # 끝까지 오면
    if currIdx == n:
        res = max(res, movePlayer())
        return

    for i in range(k):
        players.append(i)
        choosePlayer(currIdx+1)
        players.pop()
choosePlayer(0)
print(res)