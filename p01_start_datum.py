1.3.1 핵심 인물 찾기

딕셔너리 형태로 구성된 사용자 명단이 있다. 각 사용자는 숫자로 된 고유 번호인 id와 이름을 나타내는 name으로 구성되어 있다.

useres = [
  {"id":0, "name":"Hero"},
  {"id":1, "name":"Dunn"},
  {"id":2, "name":"Sue"},
  {"id":3, "name":"Chi"},
  {"id":4, "name":"Thor"},
  {"id":5, "name":"Clive"},
  {"id":6, "name":"Hicks"},
  {"id":7, "name":"Devin"},
  {"id":8, "name":"Kate"},
  {"id":9, "name":"Klein"}
]
그리고 id의 쌍으로 구성된 친구 관계의 데이터인 friendship_pairs도 있다.

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

예를 들어 (0,1)은 id가 0인 데이터 과학자 Hero와 id가 1인 데이터 과학자 Dunn이 서로 친구라는 것을 의미한다.

사용자별로 비어 있는 친구 목록 리스트를 지정하여 딕셔너리를 초기화
friendship = {user["id]:[] for user in user}
                   
friendship_pairs 내 쌍을 차례대로 살펴보면서 딕셔너리 안에 추가
for i, j in friendship_pairs:
                   friendship[i].append(j)
                   friendship[j].append(i)
  
이렇게 각 사용자의 친구 목록을 딕셔너리로 만들면 '네트워크상에서 각 사용자의 평균 연결 수는 몇 개인가?' 와 같이 네트워크의 특성에 관한 질문에 답할 수 있다.                   
  

