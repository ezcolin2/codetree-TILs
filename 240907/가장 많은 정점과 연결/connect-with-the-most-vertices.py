import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# (정수, 정점 번호) 기준으로 리스트 만들고 정렬
nodes = []
for i in range(1, n+1):
    nodes.append((arr[i], i))
nodes.sort()

# union find
uf = [i for i in range(n+1)]
# sz[i] : 뤁르 노드가 i인 그룹의 원소 개수
sz = [1 for _ in range(n+1)]
# 루트 노드 찾기
def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]

# 그룹화
for _ in range(m):
    a, b = map(int, input().split())
    root_a = find_root(a)
    root_b = find_root(b)
    uf[root_a] = root_b
    sz[root_b] += sz[root_a]

# 모든 정점이 연결되기 위한 최소 비용
min_val = 0
# 가장 작은 정수를 가진 정점부터 조사한다.
val, min_val_node = nodes[0]

# nodes의 마지막은 필요없는 값
for i in range(1, n):
    root_min_val_node = find_root(min_val_node)
    root_node = find_root(nodes[i][1])
    # 같은 그룹이라면 패스
    if root_node == root_min_val_node:
        continue
    # 다른 그룹이라면 연결 후 min_val에 추가
    uf[root_node] = root_min_val_node
    sz[root_min_val_node] += sz[root_node]
    min_val += val + nodes[i][0]
    if sz[root_min_val_node] == n:
        break

print(min_val if min_val <= k else "NO")