# 문제 제목 : 두 개 뽑아서 더하기
# 난이도 : Level 1
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    add_numbers = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            add_numbers.append(numbers[i] + numbers[j])

    unique_add_numbers = set(add_numbers)
    return sorted(unique_add_numbers)



# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 4, 1], [2, 3, 4, 5, 6, 7]),
        ([5, 0, 2, 7], [2, 5, 7, 9, 12])
    ]

    for inputs, expected in test_cases:
        num1 = inputs
        result = solution(num1)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")