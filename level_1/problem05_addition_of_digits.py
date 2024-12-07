# 문제 제목 : 자릿수 더하기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    return sum(int(i) for i in str(n))


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((1234), 10),
        ((930211), 16),
        ((8400144), 21)
    ]

    for inputs, expected in test_cases:
        n = inputs
        result = solution(n)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
