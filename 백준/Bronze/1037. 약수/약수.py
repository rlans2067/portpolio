def find_N(divisors):
    # 진짜 약수 중 가장 작은 값과 가장 큰 값의 곱은 N이 됨
    N = min(divisors) * max(divisors)
    return N

# 입력 처리
num_divisors = int(input())
divisors = list(map(int, input().split()))

# N을 찾아 출력
result = find_N(divisors)
print(result)
