def count_digits(N):
    length = len(str(N))  # 주어진 수 N의 자릿수
    total_digits = 0  # 총 자릿수
    
    # 1부터 9까지의 수는 한 자리
    for i in range(1, length):
        total_digits += i * 9 * 10**(i - 1)
    
    # 10**(length-1)부터 N까지의 수는 length 자리
    total_digits += length * (N - 10**(length - 1) + 1)
    
    return total_digits

# 입력값 설정
N = int(input())

# 결과 출력
print(count_digits(N))
