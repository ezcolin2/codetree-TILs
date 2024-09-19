import sys
input = sys.stdin.readline
a = [False] + list(input().rstrip())
b = [False] + list(input().rstrip())
arr = list(map(int, input().split()))

# 순서에 맞게 문자를 지운다.
def remove_elements(string, elements):
    new_string = string[:]
    for element in elements:
        new_string[element] = False
    return new_string

# string이 base_string의 부분 문자열인지
def is_substring(base_string, string):
    base_idx, idx = 1, 1
    while base_idx < len(base_string) and idx < len(string):
        # 삭제 되었다면 패스
        if not base_string[base_idx]:
            base_idx += 1
            continue
        # 같지 않다면 패스
        if base_string[base_idx] != string[idx]:
            base_idx += 1
            continue
        # 삭제되지도 않았고 똑같다면 
        base_idx += 1
        idx += 1
    # 반복이 끝났을 때 string을 모두 순회했다면 부분문자열이 맞음
    if idx == len(string):
        return True
    return False

# 이분 탐색
def parametric_search(a, b, arr):
    max_length = 0
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        elements = arr[:mid]
        # 제거한 새로운 문자열
        new_string = remove_elements(a, elements)
        res = is_substring(new_string, b)
        # 부분 문자열이라면 늘림
        if res:
            left = mid+1
            max_length = max(max_length, mid+1)
            continue
        # 아니라면 줄임
        right = mid-1
    return max_length
print(parametric_search(a, b, arr))