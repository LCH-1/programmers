# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    idx = 0

    while idx + 4 <= len(ingredient):
        if ingredient[idx:idx+4] == [1, 2, 3, 1]:
            del ingredient[idx:idx+4]
            idx -= 3
            answer += 1

        idx += 1

    return answer
