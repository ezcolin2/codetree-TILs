import sys
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [i for i in range(n+1)]
def find(x):
    # root 노드라면
    if uf[x]==x:
        return x
    # root 노드가 아니라면 일단 root 노드 찾아서 부모 변경
    root_node = find(uf[x])
    uf[x] = root_node
    return find(uf[x])
for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        x = find(a)
        y = find(b)
        uf[x] = y
    else:
        x = find(a)
        y = find(b)
        print(1 if x== y else 0)