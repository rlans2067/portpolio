def find_multiple(n):
    i = 1
    while True:
        multiple = int('1' * i)
        if multiple % n == 0:
            return len(str(multiple))
        i += 1

# 여러 개의 테스트 케이스를 처리
while True:
    try:
        n = int(input())
        result = find_multiple(n)
        print(result)
    except EOFError:
        break