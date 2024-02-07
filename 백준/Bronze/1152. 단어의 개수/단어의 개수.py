# 입력 문자열 받기
input_string = input().strip()

# 입력 문자열을 공백을 기준으로 나누어 리스트로 만든다
words = input_string.split()

# 단어의 개수 출력
print(len(words))
