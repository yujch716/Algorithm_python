# 문제 제목 : 문자 반복 출력하기
# 난이도 : Level 0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    return "".join([char * n for char in my_string])


# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (("hello", 3), "hhheeellllllooo")
    ]

    for inputs, expected in test_cases:
        my_string, n = inputs
        result = solution(my_string, n)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
