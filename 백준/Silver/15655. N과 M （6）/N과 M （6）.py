def backtracking(arr, M, result, start):
    # 수열이 길이 M에 도달하면 출력하고 종료
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # 가능한 모든 수에 대해 수열을 만들어나감
    for i in range(start, len(arr)):
        backtracking(arr, M, result + [arr[i]], i + 1)

def main():
    N, M = map(int, input().split())  # N과 M 입력
    arr = list(map(int, input().split()))  # N개의 수 입력
    arr.sort()  # 입력된 수열을 정렬
    backtracking(arr, M, [], 0)  # 백트래킹 함수 호출, 시작 인덱스는 0

if __name__ == "__main__":
    main()
