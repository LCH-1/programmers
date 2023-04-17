# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = [x for x in range(1, len(privacies)+1)]
    terms = {x.split(" ")[0]: int(x.split(" ")[1]) for x in terms}
    t_y, t_m, t_d = map(lambda x: int(x), today.split("."))

    for n, i in enumerate(privacies, 1):
        date, term = i.split(" ")
        term_month = terms[term]
        y, m, d = map(lambda x: int(x), date.split("."))

        d -= 1
        if d < 1:
            d = 28
            m -= 1

        m += term_month
        y += m // 12
        m %= 12

        if m < 1:
            m += 12
            y -= 1

        if y > t_y or y == t_y and m > t_m or y == t_y and m == t_m and d >= t_d:
            answer.remove(n)
            continue

    return answer
