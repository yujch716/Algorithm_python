# 문제 제목 : 배열의 유사도
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    return len(set(s1) & set(s2))


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((["a", "b", "c"], ["com", "b", "d", "p", "c"]), 2),
        ((["n", "omg"], ["m", "dot"]), 0),
        ((["he", "l", "lo"], ["hi", "he", "ho"]), 1)
    ]

    for inputs, expected in test_cases:
        s1, s2 = inputs
        result = solution(s1, s2)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
