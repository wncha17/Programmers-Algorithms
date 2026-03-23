def solution(participant, completion):
    dict_map = {}
    for p in participant:
        dict_map[p] = dict_map.get(p, 0) + 1 # p가 없으면 0, 있으면 기존값 + 1
    for c in completion:
        dict_map[c] -= 1
    for key, val in dict_map.items():
        if val > 0: return key