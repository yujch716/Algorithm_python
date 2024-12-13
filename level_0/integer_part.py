# 문제 제목 : 정수 부분
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181850

def solution(flo):
    return int(flo)


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((1.42), 1),
        ((69.32), 69),
        ((4.958), 4)
    ]

    for inputs, expected in test_cases:
        flo = inputs
        result = solution(flo)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
