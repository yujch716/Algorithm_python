# 문제 제목 : 개미 군단
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    ant1 = hp // 5
    hp = hp % 5

    ant2 = hp // 3
    hp = hp % 3

    ant3 = hp

    return ant1 + ant2 + ant3


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((23), 5),
        ((24), 6),
        ((999), 201),
        ((2), 2),
        ((4), 2)
    ]

    for inputs, expected in test_cases:
        hp = inputs
        result = solution(hp)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
