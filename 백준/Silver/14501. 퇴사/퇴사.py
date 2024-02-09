def max_profit(day, schedule):
    if day == len(schedule):  # 기저 조건: 모든 상담을 확인한 경우
        return 0
    elif day > len(schedule):  # 기저 조건: 상담 일정을 벗어난 경우
        return -float('inf')
    
    # 현재 날짜에 상담을 하는 경우와 상담을 하지 않는 경우를 비교하여 더 큰 값 선택
    profit_with_current = 0
    if day + schedule[day][0] <= len(schedule):
        profit_with_current = schedule[day][1] + max_profit(day + schedule[day][0], schedule)
    
    profit_without_current = max_profit(day + 1, schedule)
    
    return max(profit_with_current, profit_without_current)  # 현재 상담을 선택한 경우와 선택하지 않은 경우 중에서 더 큰 값 반환

N = int(input())  # N을 입력받음

# 각 날짜별로 Ti와 Pi를 저장할 리스트
schedule = []
for _ in range(N):
    Ti, Pi = map(int, input().split())  # Ti와 Pi를 입력받음
    schedule.append((Ti, Pi))  # 입력받은 Ti와 Pi를 리스트에 추가

print(max_profit(0, schedule))  # 백준이가 얻을 수 있는 최대 이익 출력
