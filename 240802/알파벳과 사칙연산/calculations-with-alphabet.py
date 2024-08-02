import sys
from collections import deque
input = sys.stdin.readline

input_arr = deque(list(input()))
if len(input_arr)==1:
    print(4)
    exit()
# 순서대로 a, b, c, d, e, f에 대한 값
arr = []

# arr에 있는 값들을 바탕으로 계산을 진행
def calculate():
    new_arr = deque()
    # 문자를 모두 숫자로 변경
    for i in range(len(input_arr)):
        # 문자라면 숫자로 변경
        if input_arr[i] not in ['+', '-', '*']:
            new_arr.append(arr[ord(input_arr[i])-ord('a')])
        # 연산자라면 그냥 넣음
        else:
            new_arr.append(input_arr[i])
    operator = '' # 연산자
    temp = [0, 0] # 숫자 보관할 곳
    res = 0 # 계산 결과
    # arr가 모두 빌 때까지 반복
    while len(new_arr) > 1:
        first = new_arr.popleft()
        operator = new_arr.popleft()
        second = new_arr.popleft()
        # print(first, second)
        # first = arr[ord(first)-ord('a')]
        # second = arr[ord(second)-ord('a')]
        if operator == '+':
            res = first + second
        elif operator == '-':
            res = first - second
        elif operator == '*':
            res = first * second
        new_arr.appendleft(res)
    return res
cal_res = -sys.maxint
# 선택
def choose(num):
    global cal_res
    # a, b, c, d, e, f 다 뽑았다면
    if num == 6:
        cal_res = max(cal_res, calculate())
        return
    
    # 아직 모두 뽑지 않았다면 1에서 4중에서 넣음
    for i in range(1, 5):
        arr.append(i)
        choose(num+1)
        arr.pop()
choose(0)
print(cal_res)