# 문제 제목 : 실패율
# 난이도 : Level 1
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    player = len(stages)
    failure_rate = {}

    for stage in range(1, N + 1):
        stuck = stages.count(stage)

        if player == 0:
            failure_rate[stage] = 0
        else:
            failure_rate[stage] = stuck / player

        player -= stuck

    answer = sorted(failure_rate, key=failure_rate.get, reverse=True)
    return answer


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ((5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5]),
        ((4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])
    ]

    for inputs, expected in test_cases:
        N, stages = inputs
        result = solution(N, stages)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
