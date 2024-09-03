import sys
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [i for i in range(n+1)]
def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]

for i in range(1, m+1):
    x, y = map(int, input().split())
    x_root = find_root(x)
    y_root = find_root(y)
    # 사이클이 생겼다면
    if x_root == y_root:
        print(i)
        exit()
    uf[x_root] = y_root
print("happy")