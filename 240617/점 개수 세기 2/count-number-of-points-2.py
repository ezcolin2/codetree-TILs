# x와 y로 나누어 모든 점에 대해 좌표 압축을 진행한다.
# 각각에 대해서 나온 모든 점들을 배열에 넣고 정렬한다.
# 그 인덱스가 곧 압축한 점이 된다.
# x1, y1, x2, y2를 압축 점으로 구한다.
# 각각의 점은 좌표 압축 리스트를 탐색한다.
# 좌상단 좌표는 자기보다 처음으로 같거나 큰 값의 인덱스, 우하단 좌표는 자기보다 처음으로 같거나 작은 값의 인덱스 
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
n, q = map(int, input().split())
dots = [list(map (int, input().split())) for _ in range(n)]
dots.sort(); # 정렬
squares = [list(map (int, input().split())) for _ in range(q)]

# 아래 값의 인덱스가 곧 압축한 점이 됨
comprehension_x = []
comprehension_y = []
for x, y in dots:
    comprehension_x.append(x)
    comprehension_y.append(y)
comprehension_x.sort()
comprehension_y.sort()

# 실제 점 -> 압축 점
mapper_x = {}
mapper_y = {}
# 인덱스 0은 모두 비워야 하니까 1부터
for idx, x in enumerate(comprehension_x):
    mapper_x[x] = idx+1
for idx, y in enumerate(comprehension_y):
    mapper_y[y] = idx+1

# 누적합 계산
prefix_sum = [[0 for _ in range(len(comprehension_y)+1)] for _ in range(len(comprehension_x)+1)]
for x, y in dots:
    new_x, new_y = mapper_x[x], mapper_y[y]
    prefix_sum[new_x][new_y] += 1

for x in range(1, len(comprehension_x)+1):
    for y in range(1, len(comprehension_y)+1):
        prefix_sum[x][y] += prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1]

# 구하기
for x1, y1, x2, y2 in squares:
    new_x1 = bisect_left(comprehension_x, x1)+1
    new_y1 = bisect_left(comprehension_y, y1)+1
    new_x2 = bisect_right(comprehension_x, x2)
    new_y2 = bisect_right(comprehension_y, y2)
    print(prefix_sum[new_x2][new_y2]-prefix_sum[new_x1-1][new_y2]-prefix_sum[new_x2][new_y1-1]+prefix_sum[new_x1-1][new_y1-1])