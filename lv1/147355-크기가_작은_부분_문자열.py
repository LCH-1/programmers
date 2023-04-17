# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    return len([int(t[i:x]) for i, x in enumerate(range(len(p), len(t)+1)) if int(t[i:x]) <= int(p)])
