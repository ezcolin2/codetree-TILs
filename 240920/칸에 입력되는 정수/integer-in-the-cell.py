n = int(input())
m = int(input())
# uf[i] : i보다 작은 곳에 넣을 수 있는 최대 숫자
uf = [i for i in range(n+1)]
def find_root(x):
    if uf[x] == x:
        return x
    uf[x] = find_root(uf[x])
    return uf[x]
res = 0 # 넣은 공의 수
for _ in range(m):
    temp = int(input())
    root = find_root(temp)
    if uf[root] == 0:
        print(res)
        exit()
    uf[root] -= 1
    res+=1
print(res)