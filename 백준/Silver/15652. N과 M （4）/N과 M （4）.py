def backtracking(N, M, result, start):
    # 수열이 길이 M에 도달하면 출력하고 종료
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # 가능한 모든 수에 대해 수열을 만들어나감
    for i in range(start, N + 1):
        backtracking(N, M, result + [i], i)

def main():
    N, M = map(int, input().split())  # N과 M 입력
    backtracking(N, M, [], 1)  # 백트래킹 함수 호출, 시작 수는 1

if __name__ == "__main__":
    main()
