# 문제 제목 : 최댓값 만들기 (1)
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5]), 20),
        (([0, 31, 24, 10, 1, 9]), 744),
        (([4, 6, 12, 5, 6]), 72)
    ]

    for inputs, expected in test_cases:
        numbers = inputs
        result = solution(numbers)
        assert result == expected, f"실패: 입력값={numbers}, 기대값={expected}, 결과값={result}"
    print("성공!")