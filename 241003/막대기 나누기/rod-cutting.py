n = int(input())
arr = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    for j in range(i):
        arr[i] = max(arr[i], arr[j] + arr[i-j])
print(arr[n])