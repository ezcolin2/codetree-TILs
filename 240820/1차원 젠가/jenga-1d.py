import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

s1, e1 = map(lambda x : int(x) - 1, input().split())
s2, e2 = map(lambda x : int(x) - 1, input().split())
arr.reverse()

def eliminate(arr, s, e):
    new_arr = []
    for i in range(s, e+1):
        arr[i] = 0
    for i in arr:
        if i != 0:
            new_arr.append(i)
    return new_arr
arr = eliminate(arr, s1, e1)
arr = eliminate(arr, s2, e2)
arr.reverse()
print(len(arr))
for i in arr:
    print(i)