n, m = map(int, input().split())
uf = [i for i in range(n+1)]
def find_root(x):
    if uf[x] == x:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]
edges = [list(map(int, input().split())) for _ in range(m)]
# 가중치 오름차순 정렬
edges.sort(key=lambda x : x[2])
# 남은 간선들의 가중치들
distances = []
for a, b, distance in edges:
    # 같은 그룹으로
    root_a = find_root(a)
    root_b = find_root(b)
    # 만약 같은 그룹이라면 패스
    if root_a == root_b:
        continue
    # 다른 그룹이라면 같은 그룹으로 만들고
    uf[root_a] = root_b
    # distances 추가
    distances.append(distance)
distances.sort()
print(sum(distances[:len(distances)-1]))