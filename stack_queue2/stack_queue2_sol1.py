import math

def solution(progresses, speeds):
    # 1. 각 작업별 남은 일수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    count = 0 # 각 배포에 해당하는 작업 수
    maxDay = days[0] # 최대 소요일 저장

    # 2.
    for i in range(len(days)):
        # 최대 소요일보다 작거나 같으면 count 증가
        if days[i] <= maxDay:
            count += 1
        # 그렇지 않다면 answer에 추가, count 초기화, 최대소요일 변경
        else:
            answer.append(count)
            count = 1
            maxDay = days[i]
        
    # 3. 마지막으로 count된 작업들을 answer에 추가
    answer.append(count)
    return answer
