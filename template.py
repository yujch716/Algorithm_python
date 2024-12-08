# 문제 제목 :
# 난이도 : Level 0
# 링크 :

def solution(num1):
    return num1


# 테스트 코드
if __name__ == "__main__":
    test_cases = [

    ]

    for inputs, expected in test_cases:
        num1 = inputs
        result = solution(num1)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
