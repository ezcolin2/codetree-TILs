import sys
input = sys.stdin.readline

n = int(input())
if n==3 or n==2:
    print(1)
    exit()
arr = [0 for i in range(n+1)]
arr[2] = 1
arr[3] = 1
for i in range(4, n+1):
    arr[i] = (arr[i-2] + arr[i-3])%10007

print(arr[n])