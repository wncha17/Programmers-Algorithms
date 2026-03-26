from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length) # 다리를 큐로 선언 (0은 빈 공간)
    trucks = deque(truck_weights) # 대기 트럭 큐
    curr_weight = 0 # 현재 다리 위 총 무게

    while trucks:
        time += 1
        # 1. 다리에서 트럭이 나감
        curr_weight -= bridge.popleft()

        # 2. 다리에 새로운 트럭이 진입할 수 있는지 확인
        if curr_weight + trucks[0] <= weight:
            new_truck = trucks.popleft()
            bridge.append(new_truck)
            curr_weight += new_truck
        else:
            # 진입 불가 시 0을 넣어 다리 길이 유지
            bridge.append(0)
    
    # 마지막 트럭이 다리에 올라간 순간 반복문이 종료되므로
    # 다리 길이(건너는 시간)만큼 더해줌
    return time + bridge_length
