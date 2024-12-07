# 문제 제목 : 점의 위치 구하기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0  and dot[1] > 0:
        return 2
    elif dot[0] > 0  and dot[1] < 0:
        return 4
    else:
        return 3



# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([2,4]), 1),
        (([-7,9]), 2),
        (([-2,-5]), 3),
        (([1, -8]), 4)
    ]

    for inputs, expected in test_cases:
        dot = inputs
        result = solution(dot)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
