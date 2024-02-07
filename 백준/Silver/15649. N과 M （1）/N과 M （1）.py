def backtracking(N, M, result, visited):
    # 수열이 길이 M에 도달하면 출력하고 종료
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # 가능한 모든 수에 대해 수열을 만들어나감
    for i in range(1, N + 1):
        # 방문하지 않은 수에 대해서만 수열에 추가
        if not visited[i]:
            visited[i] = True
            backtracking(N, M, result + [i], visited)
            visited[i] = False

def main():
    N, M = map(int, input().split())  # N과 M 입력
    visited = [False] * (N + 1)  # 방문 여부를 저장하는 리스트
    backtracking(N, M, [], visited)  # 백트래킹 함수 호출

if __name__ == "__main__":
    main()
