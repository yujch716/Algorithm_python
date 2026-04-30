# 문제 제목 : A 강조하기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181874

def solution(myString):
    return myString.lower().replace("a", "A")


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("abstract algebra"), "AbstrAct AlgebrA"),
        (("PrOgRaMmErS"), "progrAmmers"),
        (("Hello World"), "hello world"),
        (("Banana is Good"), "bAnAnA is good")
    ]

    for inputs, expected in test_cases:
        myString = inputs
        result = solution(myString)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
