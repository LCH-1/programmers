# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    l_location = (0, 3)
    r_location = (2, 3)
    answer = ''

    for i in numbers:
        if i == 0:
            t_location = (1, 3)
        else:
            t_location = ((i-1) % 3, (i-1) // 3)

        if i in [1, 4, 7]:
            answer += "L"
            l_location = t_location

        elif i in [3, 6, 9]:
            answer += "R"
            r_location = t_location

        else:
            l_dist = abs(t_location[0]-l_location[0]) + abs(t_location[1]-l_location[1])
            r_dist = abs(t_location[0]-r_location[0]) + abs(t_location[1]-r_location[1])

            if l_dist < r_dist or l_dist == r_dist and hand == "left":
                answer += "L"
                l_location = t_location

            else:
                answer += "R"
                r_location = t_location

    return answer
