# 문제 제목 : n의 배수 고르기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    return [i for i in numlist if i % n == 0]


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((3, [4, 5, 6, 7, 8, 9, 10, 11, 12]), [6, 9, 12]),
        ((5, [1, 9, 3, 10, 13, 5]), [10, 5]),
        ((12, [2, 100, 120, 600, 12, 12]), [120, 600, 12, 12]),
        ((1, [1, 3, 14, 5, 56]), [1, 3, 14, 5, 56])
    ]

    for inputs, expected in test_cases:
        n, numlist = inputs
        result = solution(n, numlist)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
