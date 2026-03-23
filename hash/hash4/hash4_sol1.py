def solution(clothes):
    # 1. 의상 종류별로 개수를 저장할 해시 맵 생성
    closet = {}
    for name, kind in clothes:
        closet[kind] = closet.get(kind, 0) + 1
        
    # 2. 각 종류별 (개수 + 1)을 모두 곱함
    answer = 1
    for count in closet.values():
        answer *= (count + 1)
        
    # 3. 아무것도 입지 않은 경우 1을 빼고 반환
    return answer - 1
