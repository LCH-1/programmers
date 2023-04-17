# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    mbti = {
        "R": 0, "T": 0, "C": 0, "F": 0,
        "J": 0, "M": 0, "A": 0, "N": 0,
    }

    for i, j in enumerate(survey):
        choice = choices[i]
        if choice == 4:
            continue

        if choice > 4:
            mbti[j[1]] += choice-4

        else:
            mbti[j[0]] += 4-choice

    RT = "T" if mbti["T"] > mbti["R"] else "R"
    CF = "F" if mbti["F"] > mbti["C"] else "C"
    JM = "M" if mbti["M"] > mbti["J"] else "J"
    AN = "N" if mbti["N"] > mbti["A"] else "A"

    return RT + CF + JM + AN
