def solution(phone_book):
    # 1. 문자열 정렬 (사전순 정렬이 되어 접두어 관계인 것끼리 붙음)
    phone_book.sort()
    
    # 2. 인접한 두 번호만 비교
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True