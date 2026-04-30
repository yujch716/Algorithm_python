# 문제 제목 : 배열 자르기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120833

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], 1, 3), [2, 3, 4]),
        (([1, 3, 5], 1, 2), [3, 5]),
        (([2, 4, 6, 8], 2, 2), [6])
    ]

    for inputs, expected in test_cases:
        numbers, num1, num2 = inputs
        result = solution(numbers, num1, num2)
        assert result == expected, f"테스트 실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")