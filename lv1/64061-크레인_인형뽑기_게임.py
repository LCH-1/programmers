# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    basket = []
    answer = 0

    for m in moves:
        for b in board:
            if doll := b[m-1]:
                b[m-1] = 0
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break

    return answer
