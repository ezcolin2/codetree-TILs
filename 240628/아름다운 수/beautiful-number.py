import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
def find(idx):
    global cnt
    if idx == n:
       cnt += 1 
       return
    elif idx > n:
        return
    for i in range(1, 5):
        find(idx+i)
find(0)
print(cnt)