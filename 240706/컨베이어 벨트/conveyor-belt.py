import sys
input = sys.stdin.readline
n, t = map(int, input().split())
arr = list(input().split()) + list(input().split())

# 회전하는 함수
# 뒤에서부터 한 칸씩 앞으로 땡긴다.
def rotate(n):
    for _ in range(n):
        temp = arr[-1] # 마지막 값을 가져온다.
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = temp
rotate(t)

print(' '.join(arr[0:len(arr)//2]))
print(' '.join(arr[len(arr)//2:len(arr)]))