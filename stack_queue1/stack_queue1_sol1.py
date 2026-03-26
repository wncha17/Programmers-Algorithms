def solution(arr):
    stack = []
    for num in arr:
        # 스택이 비어있거나, 마지막에 넣은 숫자와 현재 숫자가 다를 때만 추가
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack