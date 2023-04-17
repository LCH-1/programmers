# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    data = {}
    answer = []

    for i, j in enumerate(s):
        if data.get(j) == None:
            data[j] = i
            answer.append(-1)
            continue

        answer.append(i-data[j])
        data[j] = i

    return answer
