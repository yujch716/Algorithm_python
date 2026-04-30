# 문제 제목 : 행렬의 곱셈
# 난이도 : Level 2
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    multiple = []
    for i in range(len(arr1)):
        row = []

        for j in range(len(arr2[0])):
            item = 0

            for k in range(len(arr2)):
                item += arr1[i][k] * arr2[k][j]

            row.append(item)
        multiple.append(row)

    return multiple



# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        (([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]), [[15, 15], [15, 15], [15, 15]]),
        (([[2, 3, 2], [4, 2, 4], [3, 1, 4]]	, [[5, 4, 3], [2, 4, 1], [3, 1, 1]]), [[22, 22, 11], [36, 28, 18], [29, 20, 14]])
    ]

    for inputs, expected in test_cases:
        num1, num2 = inputs
        result = solution(num1, num2)
        assert result == expected, f"실패: 입력값={inputs}, 기대값={expected}, 결과값={result}"
    print("성공!")
