import sys
input = sys.stdin.readline
n, t = map(int, input().split())
t %= n*3
arr = []
for _ in range(3):
    arr += list(map(int, input().split()))
new_arr = [0 for _ in range(len(arr))]
# 마지막 값 저장
temp = arr[-1]
for i in range(n*3 - 1, -1, -1):
    new_arr[i] = arr[i-t]
for i in new_arr[:n]:
    print(i, end = ' ')
print()
for i in new_arr[n:2*n]:
    print(i, end = ' ')
print()
for i in new_arr[2*n:3*n]:
    print(i, end = ' ')