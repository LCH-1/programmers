# https://school.programmers.co.kr/learn/courses/30/lessons/160585

def solution(board):
    all_board = ''.join(board)
    o_count = all_board.count('O')
    x_count = all_board.count('X')
    o_done = 0
    x_done = 0

    def done_check(target):
        nonlocal o_done, x_done

        if target.count('O') == 3:
            o_done += 1
        elif target.count('X') == 3:
            x_done += 1

    for i in board:
        done_check(i)

    for i in range(3):
        column = [x[i] for x in board]
        done_check(column)

    done_check([x[i] for i, x in enumerate(board)])
    done_check([x[i] for i, x in enumerate(board[::-1])])

    if o_count != x_count and o_count != x_count+1 or \
       o_count > 5 or \
       x_count > 4 or \
       o_done and o_count-1 != x_count or \
       x_done and o_count != x_count:

        return 0

    return 1
