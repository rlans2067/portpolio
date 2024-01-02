import math

def solution(n):
    answer = 0
    x= math.sqrt(n)
    if int(x) == x:
        x += 1
        answer = x*x
    else :
        answer = -1
    return answer