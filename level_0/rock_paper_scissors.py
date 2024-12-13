# 문제 제목 : 가위 바위 보
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    replace_map = {"0":"5", "2":"0", "5":"2"}
    return ''.join(replace_map[char] for char in rsp)


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("2"), "0"),
        (("205"), "052"),
        (("05"), "52")
    ]

    for inputs, expected in test_cases:
        rsp = inputs
        result = solution(rsp)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
