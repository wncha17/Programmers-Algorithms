def solution(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    
    unique_types = len(d.keys())
    return min(len(nums) // 2, unique_types)