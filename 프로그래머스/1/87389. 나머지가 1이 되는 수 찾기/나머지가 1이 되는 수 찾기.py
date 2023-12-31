def solution(n):
    for x in range(2, n):
        if n % x == 1 :
            answer = x
            return answer
    return n-1  