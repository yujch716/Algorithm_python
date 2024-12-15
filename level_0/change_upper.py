# 문제 제목 : 특정한 문자를 대문자로 바꾸기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    return "".join([i.upper() if i == alp else i for i in my_string])


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("programmers", "p"), "Programmers"),
        (("lowercase", "x"), "lowercase"),
        (("hello", "l"), "heLLo")
    ]

    for inputs, expected in test_cases:
        my_string, alp = inputs
        result = solution(my_string, alp)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
