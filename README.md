# DRF 스터디: `Re.duce` 프로젝트

1. #### 서비스 기획

   - 마감 세일을 도와주는 플랫폼 서비스
   - 크게 나눠보면 소비자(손님)와 공급자(사장님)가 있음
   - 소비자는 로그인을 해야 하며, `id` == `phone number` 추가 정보는 딱히 없음
   - 소비자는 세 가지 방식으로 할인 중인 메뉴를 볼 수 있음
     1. 위치를 선택해서 보는 방법
     2. 현재 위치를 기반으로 notification을 받는 방법
     3. `TODO` 특정 가게를 팔로잉해서 notification을 받는 방법
   - 공급자는 서비스에서 제공하는 인터페이스를 통해서 할인 메뉴를 설정할 수 있음
   - 필요한 뷰는 다음과 같음
     - 처음 메뉴 등록
     - 메뉴 수정
     - 할인 대상 메뉴 설정
     - 주문 내역 및 notification
   - 결제는 앱 내에서 이루어짐. `아임포트` 를 사용하여 개발할 예정

2. #### 개발 계획

   - base-url: api/

   - base-url : users/

     - `GET`  ^$ : 유저 리스트 보기
     - `POST` ^signup/$ : 회원가입
     - `POST` ^login/$ : 로그인
     - `POST` ^logout/$ : 로그아웃
     - `GET`  ^{id}/$ : 유저 프로필 보기
     - `PUT` ^{id}/$ : 유저 프로필 수정
     - `PATCH` ^{id}/$ : 유저 프로필 부분 수정

      [손님]

   - base-url: customers/

     - <u>`보류` 현재 위치 기반 알림 기능 : 공부를 하자.</u>
     - `GET` ^$: 할인 중인 메뉴 리스트
       - `query_params` 위치 기반 검색 기능
     - <u>`보류` 결제 뷰: 공부를 하자.</u>

      [사장님]

   - base-url: owners/{id}

     - `GET` ^$ : 현재 등록된 메뉴 리스트
     - <u>`POST` ^$ : 메뉴 등록</u>: `TODO` 세분화
     - <u>`POST` ^sales/$ : 할인 메뉴 추가</u>: `TODO` 세분화
     - <u>`GET` ^sales/$ : 할인 메뉴들 보기</u>: `TODO` 세분화
       - <u>`PUT` ^sales/{id}$ : 할인 메뉴 수정</u>: `TODO` 세분화
     - `GET` ^orders/$ : 주문 내역 리스트 확인
       - `GET` ^orders/{id}/$ : 주문 내역 확인
     - <u>주문 현황 알림 기능: 공부를 하자</u>

      (2단계)

   - 평점
   - 댓글
   - 팔로잉
   - 프로필
   - 재고 변동 트리거

3. #### Reqs

   - pip install django
   - pip install djangorestframework
