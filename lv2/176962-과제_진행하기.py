# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    plans.sort(key=lambda x: x[1])
    plans.append(["", "0:0", "0"])
    keep, answer = [], []

    def hour_to_minute(time_):
        hour, minute = time_.split(":")
        return int(hour) * 60 + int(minute)

    def plan_to_data(plan):
        subject, start_time, taken_time = plan
        start_time = hour_to_minute(start_time)
        taken_time = int(taken_time)

        return subject, start_time, taken_time

    c_subject, c_start_time, c_taken_time = plan_to_data(plans.pop(0))
    current_time = c_start_time

    for plan in plans:
        while keep and current_time < c_start_time:
            first_keep = keep[-1]
            if first_keep["left_time"] + current_time <= c_start_time:
                answer.append(keep.pop()["subject"])
                current_time += first_keep["left_time"]

            else:
                first_keep["left_time"] -= c_start_time - current_time
                current_time = c_start_time
                break

        n_subject, n_start_time, n_taken_time = plan_to_data(plan)

        if n_start_time < (end_time := c_start_time + c_taken_time):
            current_time = n_start_time
            keep.append({"subject": c_subject, "left_time": end_time - n_start_time})

        else:
            current_time = end_time
            answer.append(c_subject)

        c_subject, c_start_time, c_taken_time = n_subject, n_start_time, n_taken_time

    while keep:
        answer.append(keep.pop()["subject"])

    return answer

# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"], ["ddd", "20:40", "10"]]))
# print(solution([["aaa", "12:00", "20"], ["bbb", "500:5000", "30"], ["ccc", "7000:40", "10"]]))
