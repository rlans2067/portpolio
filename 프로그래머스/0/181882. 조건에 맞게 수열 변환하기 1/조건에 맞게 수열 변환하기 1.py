def solution(arr):
    answer = []
    for num in arr:
        if num >= 50 and num % 2 == 0:  # 50보다 크거나 같은 짝수
            answer.append(num // 2)
        elif num < 50 and num % 2 == 1:  # 50보다 작은 홀수
            answer.append(num * 2)
        else:
            answer.append(num)  # 나머지 경우는 그대로 유지

    return answer