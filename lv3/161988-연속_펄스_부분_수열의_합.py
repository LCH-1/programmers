# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    answer = [0]
    x = 1
    for i in sequence:
        x *= -1
        answer.append(answer[-1] + x * i)

    return abs(max(answer) - min(answer))
