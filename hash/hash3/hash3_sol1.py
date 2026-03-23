def solution(phone_book):
    # 1. 모든 번호를 해시 맵에 등록 (탐색 속도 O(1))
    hash_map = {phone: True for phone in phone_book}

    # 2. 각 번호의 접두어가 해시 맵에 있는지 확인
    for phone in phone_book:
        prefix = ""
        for digit in phone:
            prefix += digit
            # 자기 자신과 똑같은 경우는 제외하고, 잘라낸 값이 맵에 있다면 접두어 존재!
            if prefix in hash_map and prefix != phone:
                return False
        
    return True
