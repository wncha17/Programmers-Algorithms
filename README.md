## 📝 [Sorting]  (Lv. 1)
> **문제 링크:** [https://school.programmers.co.kr/learn/courses/30/lessons/42748]

### 1. 🔍 Key Signal (문제의 단서)
- **키워드:** "i번째부터 j번째까지 자르고", "정렬한 후", "k번째에 있는 수"
- **알고리즘:** 정렬(Sorting) & 슬라이싱(Slicing)
- **판단 근거:**
  1. 배열의 특정 부분집합(Subset)을 추출해야 한다.
  2. 추출된 부분집합 내에서 크기 순서를 따져야 하므로 정렬이 필수적이다.
  3. 데이터 크기가 크지 않아 파이썬의 기본 정렬(O(N logN))로 충분히 해결 가능하다.

### 2. 💡 Strategy (설계)
- **[Solution 1] 리스트 컴프리헨션을 활용한 간결한 풀이**
  - 로직: commands의 각 원소 [i, j, k]를 순회하며, 인덱스 규칙(1-based to 0-based)에 맞춰 자르고 정렬함.
  - 특징: 파이썬다운 코드로 가독성이 높으며, 실무에서 빠른 구현이 필요할 때 유용함.

### 3. ⚠️ Edge Case & Pitfalls
- 목적지에 도달할 수 없는 경우 초기값 유지 확인.
- `pop(0)` 대신 `deque.popleft()` 사용으로 효율성 확보.

### 4. 🛠️ Implementation (코드 요약)
- [링크 또는 핵심 코드 스니펫]

### 5. 🏟️ Real-world Connection
- 자율주행 차량의 장애물 회피 경로 생성 알고리즘의 기초 모델.
