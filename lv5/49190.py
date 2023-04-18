# https: // school.programmers.co.kr/learn/courses/30/lessons/49190
from collections import defaultdict


def solution(arrows):
    DIRECTION = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    answer = 0
    current = (0, 0)
    visit_history = defaultdict(lambda: False)
    location_history = set()

    visit_history[(0, 0)] = True

    for arrow in arrows:
        x, y = DIRECTION[arrow]

        # 대각선 이동일 경우 1칸씩 2번 이동
        arr = [1, 1] if arrow % 2 else [2]

        for i in arr:
            next_ = (current[0] + x*i, current[1] + y*i)

            if visit_history[next_] and (current, next_) not in location_history:
                answer += 1
            else:
                visit_history[next_] = True

            location_history |= {(current, next_), (next_, current)}

            current = next_

    return answer
