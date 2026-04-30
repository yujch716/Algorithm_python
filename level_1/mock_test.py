# 문제 제목 : 모의고사
# 난이도 : Level 1
# 링크 :

def solution(answers):
    patterns = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }

    men_correct_count = {
        man: 0 for man in patterns
    }

    for key, answer in enumerate(answers):
        for man, pattern in patterns.items():
            if answer == pattern[key % len(pattern)]:
                men_correct_count[man] += 1

    max_count = max(men_correct_count.values())

    max_count_men = [
        man for man, count in men_correct_count.items()
        if count == max_count
    ]

    return max_count_men


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5]), ([1])),
        (([1, 3, 2, 4, 2]), ([1, 2, 3]))
    ]

    for inputs, expected in test_cases:
        num1 = inputs
        result = solution(num1)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
