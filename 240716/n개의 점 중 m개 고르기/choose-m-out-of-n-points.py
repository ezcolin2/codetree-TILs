import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]

# 조합
combination = []

# 두 점 사이 거리 구하는 함수
def get_distance(dot1, dot2):
    return ((dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2)
# 현재까지 뽑은 조합에서 가장 먼 거리를 반환
def get_max_distance():
    max_distance = 0
    for i in range(len(combination)):
        for j in range(len(combination)):
            if i==j:
                continue
            
            max_distance = max(max_distance, get_distance(combination[i], combination[j]))
    return max_distance
res = sys.maxsize
# 조합 만들기
# cnt번째 원소로 dots[idx]를 선택할지 말지
def make_combination(idx, cnt):
    global res
    # 끝까지 왔다면
    if idx == n:

        # 다 뽑았다면
        if cnt == m:
            res = min(res, get_max_distance())
        return
    
    # dots[idx]를 선택
    combination.append(dots[idx])
    make_combination(idx+1, cnt+1)
    combination.pop()

    # dots[idx]를 선택하지 않음
    make_combination(idx+1, cnt)
make_combination(0, 0)
print(int(res))