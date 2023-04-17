# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    s = list(s[-1::-1])
    answer = 0
    first_str = None

    while True:
        if not first_str:
            first_str = s[-1]
            same_count = 0
            difference_count = 0

        if first_str == s.pop():
            same_count += 1
        else:
            difference_count += 1
        if same_count == difference_count:
            first_str = None
            answer += 1

        if not s:
            if same_count != difference_count:
                answer += 1
            break

    return answer
