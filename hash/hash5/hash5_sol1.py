def solution(genres, plays):
    answer = []

    # 1. 데이터 구조 설계
    genre_total = {} # 장르별 총 재생횟수
    genre_songs = {} # 장르별 [(재생횟수, 고유번호), ...]

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 총 재생 횟수 누적
        genre_total[genre] = genre_total.get(genre, 0) + play

        # 장르별 노래 정보 추가
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))

    # 2. 장르 우선순위 결정 (총 재생횟수 내림차순 정렬)
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)

    # 3. 베스트 앨범 수록
    for genre, _ in sorted_genres:
        # 장르 내 노래 정렬: 재생횟수(x[0])는 내림차순(-), 고유번호(x[1])는 오름차순(+)
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))

        # 최대 2개까지만 선택
        answer.extend(s[1] for s in songs[:2])

    return answer
