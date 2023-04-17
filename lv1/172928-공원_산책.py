# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    c_x, c_y = [(location, i) for i, x in enumerate(park) if (location := x.find("S")) != -1][0]
    DIRECTIONS = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

    def move():
        direction, n = i.split(" ")
        y, x = DIRECTIONS[direction]
        n = int(n)

        if not 0 <= c_y+y*n < len(park) or not 0 <= c_x+x*n < len(park[0]):
            return c_y, c_x

        for j in range(1, n+1):
            if park[c_y+y*j][c_x+x*j] == "X":
                return c_y, c_x

        return c_y+y*n, c_x+x*n

    for i in routes:
        c_y, c_x = move()

    answer = [c_y, c_x]
    return answer
