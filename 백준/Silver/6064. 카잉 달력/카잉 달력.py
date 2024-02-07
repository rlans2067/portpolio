def find_k(M, N, x, y):
    k = x
    while k <= M * N:
        # 현재 해의 y 값 계산
        if (k - 1) % N + 1 == y:
            return k
        # 다음 해로 이동
        k += M
    return -1

def main():
    T = int(input())  # 테스트 데이터의 수 입력
    for _ in range(T):
        M, N, x, y = map(int, input().split())  # M, N, x, y 입력
        print(find_k(M, N, x, y))  # 결과 출력

if __name__ == "__main__":
    main()
