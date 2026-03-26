def solution(progresses, speeds):
    answer = []
    max_day = 0

    for p, s in zip(progresses, speeds):
        day = (99 - p) // s + 1

        if day > max_day:
            answer.append(1)
            max_day = day
        else:
            answer[-1] += 1

    return answer
