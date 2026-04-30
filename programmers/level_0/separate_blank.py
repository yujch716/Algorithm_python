# 문제 제목 : 공백으로 구분하기 1
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181869

def solution(my_string):
    return my_string.split(' ')


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("i love you"), ["i", "love", "you"]),
        (("programmers"), ["programmers"]),
        (("hello world"), ["hello", "world"])
    ]

    for inputs, expected in test_cases:
        num1 = inputs
        result = solution(num1)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
