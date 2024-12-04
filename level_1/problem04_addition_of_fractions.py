# 문제 제목 : 분수의 덧셈
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120808

import math
def solution(numer1, denom1, numer2, denom2):
    denominator = denom1 * denom2
    numerator = (numer1 * denom2) + (numer2 * denom1)
    divisor = math.gcd(numerator, denominator)

    return [numerator//divisor, denominator//divisor]


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((1,2,3,4), [5, 4]),
        ((9,2,1,3), [29, 6])
    ]

    for inputs, expected in test_cases:
        numer1, denom1, numer2, denom2 = inputs
        result = solution(numer1, denom1, numer2, denom2)
        assert result == expected, f"실패: 입력값={numer1, denom1, numer2, denom2}, 기대값={expected}, 결과값={result}"

    print("성공!")