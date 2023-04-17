# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost_del = set(lost) - set(reserve)
    reserve_del = set(reserve) - set(lost)

    for i in reserve_del:
        if (j := i-1) in lost_del or (j := i+1) in lost_del:
            print(j)
            lost_del.remove(j)
            continue

    return n - len(lost_del)
