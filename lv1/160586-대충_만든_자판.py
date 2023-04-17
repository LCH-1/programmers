# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []

    def check(target):
        result = 0
        for i in target:
            if count := key_memory.get(i):
                result += count
                continue

            try:
                count = min([y for x in keymap if (y := x.find(i)) != -1]) + 1
            except:
                return -1

            key_memory[i] = count
            result += count

        return result

    for target in targets:
        key_memory = {}
        answer.append(check(target))

    return answer
