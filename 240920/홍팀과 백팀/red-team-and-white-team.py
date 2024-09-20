n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

uf = [i for i in range(n+1)]
def find_root(x):
    if uf[x] == x:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]

# 모든 정점에 연결된 점들을 보고 같은 그룹인지 확인
for node in range(1, n+1):
    # 첫 번째 연결된 노드
    if not graph[node]:
        continue
    temp_root = find_root(graph[node][0])
    for next_node in graph[node]:
        root_node = find_root(node)
        root_next_node = find_root(next_node)
        # 같은 그룹이면 모순
        if root_node == root_next_node:
            print(0)
            exit()
        # 모순이 아니면 first_next_node를 루트로
        uf[next_node] = temp_root
print(1)