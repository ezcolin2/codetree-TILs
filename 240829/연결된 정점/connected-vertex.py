import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# union find
uf = [i for i in range(n+1)]

# 루트 노드를 기준으로 해당 그룹의 사이즈
group_size = [1 for _ in range(n+1)]

def find_root(x):
    # 루트 노드라면 그댇로 반환
    if x == uf[x]:
        return x
    # 루트 노드가 아니라면
    root_node = find_root(uf[x])
    uf[x] = root_node
    return root_node

def union(a, b):
    root_a = find_root(a)
    root_b = find_root(b)
    uf[root_a] = root_b
    group_size[root_b] += group_size[root_a]

for _ in range(m):
    op = list(input().split())
    if op[0] == 'x':
        a, b = int(op[1]), int(op[2])
        union(a, b)
    else:
        a = int(op[1])
        print(group_size[find_root(a)])