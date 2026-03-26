def solution(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        # 중간에 음수가 되면 ')'가 '('보다 먼저 나온 것이므로 실패
        if balance < 0:
            return False
            
    return balance == 0