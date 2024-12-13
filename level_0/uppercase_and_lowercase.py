# 문제 제목 : 대문자와 소문자
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    return my_string.swapcase()


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("cccCCC"), "CCCccc"),
        (("abCdEfghIJ"), "ABcDeFGHij"),
        (("HellO"), "hELLo")
    ]

    for inputs, expected in test_cases:
        my_string = inputs
        result = solution(my_string)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
