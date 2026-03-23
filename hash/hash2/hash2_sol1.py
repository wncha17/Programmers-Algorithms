def solution(nums):
    # 1. 내가 가질 수 있는 최대 종류의 수는 N/2마리
    max_take = len(nums) // 2
    
    # 2. 실제로 존재하는 폰켓몬의 종류 수 (중복 제거)
    unique_types = len(set(nums))
    
    # 3. 둘 중 더 작은 값이 정답 (종류가 아무리 많아도 N/2까지만 가져가니까)
    return min(max_take, unique_types)