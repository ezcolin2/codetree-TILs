import sys
input = sys.stdin.readline
def find_root(x):
    # 루트 노드라면
    if uf[x] == x:
        return x
    # 루트 노드가 아니라면 일단 부모를 root 노드로 변경
    root_node = find_root(uf[x])
    uf[x] = root_node
    return root_node
n, m, k = map(int, input().split())
uf = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    x_root = find_root(x)
    y_root = find_root(y)
    uf[x_root] = y_root

sequence = map(int, input().split())

s = set()
for i in sequence:
    s.add(find_root(i))
print(1 if len(s)==1 else 0)