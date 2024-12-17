# 문제 제목 : 순서쌍의 개수
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120836

import math
def solution(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)

    return len(divisors)



# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((20), 6),
        ((100), 9),
        ((15), 4)
    ]

    for inputs, expected in test_cases:
        n = inputs
        result = solution(n)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
