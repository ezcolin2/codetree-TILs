import sys
input = sys.stdin.readline
n = int(input())
uf = [i for i in range(n+1)]
arr = [list(map(int, input().split())) for _ in range(n-2)]
arr.sort()

# 어떠한 그룹의 루트 노드 
s = set()

def find_root(x):
    if x == uf[x]:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]
for dots in arr:
    # 가장 작은 값을 루트로
    a, b = min(dots), max(dots)
    root_a = find_root(a)
    root_b = find_root(b)
    uf[root_b] = root_a
    s.add(root_a)
res = list(s)
res.sort()
print(res[0], res[1])