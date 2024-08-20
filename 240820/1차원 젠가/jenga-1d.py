import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# arr[s]에서 arr[e] 블록을 빼고 난 뒤 
def eliminate(arr, s, e):
    new_arr = []
    # 0으로 만듦
    for i in range(len(arr) - s, len(arr) - e - 1, -1):
        arr[i] = 0
    # 0이 아닌 경우만 new_arr에 추가
    for i in arr[::-1]:
        if i != 0:
            new_arr.append(i)
    return new_arr

arr = eliminate(arr, s1, e1)
arr = eliminate(arr, s2, e2)
print(len(arr))
for i in arr:
    print(i)