# 문제 제목 : 최빈값 구하기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    frequency = {}
    for i in array:
        frequency[i] = frequency.get(i, 0) + 1

    max_value = max(frequency.values())
    max_keys = [key for key, value in frequency.items() if value == max_value]

    if len(max_keys) > 1:
        max_value_key = -1
    else:
        max_value_key = next(iter(max_keys))

    return max_value_key


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 3, 3, 4]), 3),
        (([1, 1, 2, 2]), -1),
        (([1]), 1),
        (([-3, -5, -3, 4, 45]), -3)
    ]

    for inputs, expected in test_cases:
        array = inputs
        result = solution(array)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
