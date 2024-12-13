# 문제 제목 : 가장 큰 수 찾기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    max_num = array[0]
    max_num_index = 0

    for i in range(0, len(array)):
        if array[i] > max_num:
            max_num = array[i]
            max_num_index = i

    return [max_num, max_num_index]


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([1, 8, 3]), [8, 1]),
        (([9, 10, 11, 8]), [11, 2]),
        (([2, 4, 6, 8]), [8, 3])
    ]

    for inputs, expected in test_cases:
        array = inputs
        result = solution(array)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
