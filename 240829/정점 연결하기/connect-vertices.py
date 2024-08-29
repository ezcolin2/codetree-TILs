import sys
input = sys.stdin.readline
n = int(input())
uf = [i for i in range(n+1)]
arr = [list(map(int, input().split())) for _ in range(n-2)]
groups = [[i] for i in range(n+1)]

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
    groups[root_a] += groups[root_b]
group = groups[find_root(1)]
group.sort()
if group[0] != 1:
    print(1, group[0])
else:
    for i in range(1, len(group)):
        # 중간에 비어있는겍 존재한다며 
        if group[i] != group[i-1]+1:
            print(min(group[0], group[i]-1), max(group[0], group[i]-1))
            exit()
    print(1, group[-1] + 1)