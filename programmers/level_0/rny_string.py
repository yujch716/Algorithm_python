# 문제 제목 : rny_string
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181863

def solution(rny_string):
    return rny_string.replace('m', 'rn')


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("masterpiece"), "rnasterpiece"),
        (("programmers"), "prograrnrners"),
        (("jerry"), "jerry"),
        (("mom"), "rnorn")
    ]

    for inputs, expected in test_cases:
        num1 = inputs
        result = solution(num1)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
