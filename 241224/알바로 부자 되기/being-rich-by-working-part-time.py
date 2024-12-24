# 날짜의 범위가 너무 크기 때문에 압축한다.
def compression(part_times):
    # 모든 날짜를 리스트에 넣는다.
    dates = []
    for start, end, _ in part_times:
        dates.append(start)
        dates.append(end)
    
    # 정렬한다.
    dates.sort()

    # 변환 맵
    transform_map = {}
    current = 0

    # 중복 제거를 위한 집합
    date_set = set()
    
    for date in dates:
        # 나왔다면 continue
        if date in date_set:
            continue
        date_set.add(date) # set에 추가
        transform_map[date] = current # 압축
        current += 1 

    return transform_map
n = int(input())
part_times = [list(map(int, input().split())) for _ in range(n)]

# 현재 시점이전에 0이 아닌 값이 나올 때 그 값을 반환
def find_max_before(dp, date):
    # for i in range(date, -1, -1):
    #     if dp[i] != 0:
    #         return dp[i]
    # return 0
    return max(dp[:date+1])

# 최대 값 구하기 
def solution(part_times, length):
    dp = [0]*length
    for start, end, money in part_times:
        dp[end] = max(dp[end], max(dp[:start] if start > 0 else [0])+money)
    return max(dp)

# 압축한다.
comprehension_dates = compression(part_times)
for i in range(len(part_times)):
    part_times[i][0] = comprehension_dates[part_times[i][0]]
    part_times[i][1] = comprehension_dates[part_times[i][1]]

print(solution(part_times, len(comprehension_dates)))