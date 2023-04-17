# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    data = {}

    for i in array:
        try:
            data[i] += 1
        except:
            data[i] = 1

    data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    return -1 if len(data) > 1 and data[0][1] == data[1][1] else data[0][0]
