# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''

    skip = [ord(x) for x in skip]

    for i in s:
        i_num = ord(i)
        for _ in range(index):
            i_num += 1
            while True:
                if i_num in skip:
                    i_num += 1
                    continue

                if i_num > 122:
                    i_num -= 26
                    continue

                break

        answer += chr(i_num)

    return answer
