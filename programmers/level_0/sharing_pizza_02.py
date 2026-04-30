# 문제 제목 : 피자 나눠 먹기 (2)
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120815

import math


def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((6), 1),
        ((10), 5),
        ((5), 5)
    ]

    for inputs, expected in test_cases:
        n = inputs
        result = solution(n)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
