def backtracking(arr, M, result):
    # 수열이 길이 M에 도달하면 출력하고 종료
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # 가능한 모든 수에 대해 수열을 만들어나감
    for i in range(len(arr)):
        backtracking(arr, M, result + [arr[i]])

def main():
    N, M = map(int, input().split())  # N과 M 입력
    arr = list(map(int, input().split()))  # N개의 수 입력
    arr.sort()  # 입력된 수열을 정렬
    backtracking(arr, M, [])  # 백트래킹 함수 호출

if __name__ == "__main__":
    main()
