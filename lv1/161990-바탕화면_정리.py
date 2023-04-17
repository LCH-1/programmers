# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    luy, lux = len(wallpaper[0]), len(wallpaper)
    rdy, rdx = 0, 0

    for i, x in enumerate(wallpaper):
        r = [j for j, y in enumerate(x) if y == "#"]
        if not r:
            continue
        if len(r) == 1:
            s, e = r[0], r[0]
        else:
            s, e = r[0], r[-1]

        if s < luy:
            luy = s
        if i < lux:
            lux = i
        if e > rdy:
            rdy = e
        if i > rdx:
            rdx = i

    answer = [lux, luy, rdx+1, rdy+1]
    return answer
