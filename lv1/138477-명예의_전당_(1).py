# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    result = []
    boundary = None

    for i in score:
        if boundary == None:
            boundary = i

        if len(answer) < k:
            answer.append(i)
            if boundary > i:
                boundary = i

        elif i > boundary:
            answer.pop(answer.index(boundary))
            answer.append(i)
            boundary = min(answer)

        result.append(boundary)

    return result
