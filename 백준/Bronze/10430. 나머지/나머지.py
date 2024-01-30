def calculate_values(A, B, C):
    result1 = (A + B) % C
    result2 = ((A % C) + (B % C)) % C
    result3 = (A * B) % C
    result4 = ((A % C) * (B % C)) % C
    return result1, result2, result3, result4

# 입력 받기
A, B, C = map(int, input().split())

# 결과 계산
result_values = calculate_values(A, B, C)

# 결과 출력
for result in result_values:
    print(result)
