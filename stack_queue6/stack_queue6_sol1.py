def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 인덱스를 저장할 스택

    for i in range(n):
        # 스택이 비어있지 않고, 현재 가격이 스택 맨 위(이전 가격)보다 떨어졌다면
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            # 기간 계산: 현재 인덱스 - 기록된 인덱스
            answer[top] = i - top
        
        # 현재 인덱스를 스택에 추가
        stack.append(i)

    # 끝까지 가격이 떨어지지 않은 인덱스들 처리
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer
