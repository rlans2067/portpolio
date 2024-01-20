def solution(sides):
    # 주어진 세 변의 길이를 정렬합니다.
    sides.sort()

    # 가장 긴 변의 길이
    max_side = sides[2]

    # 나머지 두 변의 길이의 합
    sum_of_other_sides = sides[0] + sides[1]

    # 삼각형을 만들 수 있는지 여부를 판단합니다.
    if max_side < sum_of_other_sides:
        return 1  # 삼각형을 만들 수 있음
    else:
        return 2  # 삼각형을 만들 수 없음