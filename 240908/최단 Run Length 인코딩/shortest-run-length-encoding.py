import sys
input = sys.stdin.readline
input_string = input()

def right_shift(input_string, count):
    length = len(input_string)
    input_list = list(input_string)
    res_list = [0]*length
    # 횟수만큼 밀어서 넣기
    for i in range(length):
        res_list[i] = input_list[i-2]
    return ''.join(res_list)

# Run-Length Encodoing을 적용한 후 생성된 문자열 길이
def run_length_encoding(input_string):
    left, right = 0, 0
    res_string = "" # 결과
    # 문자열 끝까지 조사
    while right < len(input_string):
        # 만약 같다면
        if input_string[left] == input_string[right]:
            right += 1
            continue
        # 다르다면
        res_string += input_string[left]
        res_string += str(right-left)
        left = right
    # 다 끝났는데 left와 right가 같지 않다면
    if left < right:
        res_string += input_string[left]
        res_string += str(right-left)
    return res_string

min_length = sys.maxsize
for i in range(len(input_string)):
    shifted_res = right_shift(input_string, i)
    run_length_encoding_result = run_length_encoding(shifted_res)
    min_length = min(min_length, len(run_length_encoding_result))
print(min_length)