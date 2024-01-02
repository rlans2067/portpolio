def solution(n):
    answer = 0
    a = list(str(n))
    a = sorted(a, reverse = True)
    answer = int(''.join(a))
    return answer