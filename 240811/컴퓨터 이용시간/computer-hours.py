import sys
import heapq
input = sys.stdin.readline
n = int(input())
input_arr = [list(map(int, input().split())) for i in range(n)]

# [시작 시간, 1, 사용자 번호] [종료 시간, -1, 사용자 번호]의 배열을 만들고 시간 순서대로 정렬한다.
arr = []
for idx, (start, end) in enumerate(input_arr):
    arr.append([start, 1, idx])
    arr.append([end, -1, idx])
arr.sort()

# res[x]의 의미 : x번째 사용자가 사용한 컴퓨터 번호
res = [-1 for _ in range(n)]

# 우선순위 큐 
queue = [i+1 for i in range(n)]
heapq.heapify(queue)

# 사용자 번호마다 배정받은 컴퓨터 번호
computer_number = 1

for start, flag, idx in arr:
    
    # 만약 시작 시간이라면
    if flag == 1:
        # 우선순위 큐에서 가장 작은 값 빼서 배정
        number = heapq.heappop(queue)
        res[idx] = number

    # 만약 종료 시간이라면
    else:
        # 배정받은 번호 반납 
        heapq.heappush(queue, res[idx])
for i in res:
    print(i, end = ' ')