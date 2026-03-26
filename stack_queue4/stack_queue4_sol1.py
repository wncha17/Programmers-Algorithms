from collections import deque

def solution(priorities, location):
    # 1. (우선순위, 원래 위치)를 큐에 저장
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        curr = queue.popleft()

        # 2. 큐 안에 현재보다 높은 우선순위가 있는지 확인
        if any(curr[0] < q[0] for q in queue):
            queue.append(curr)
        else:
            # 3. 실행 처리
            answer += 1
            if curr[1] == location:
                return answer
