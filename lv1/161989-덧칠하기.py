# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    current = section[0]

    for i in section:
        if current <= i:
            current = i + m
            answer += 1

    return answer
