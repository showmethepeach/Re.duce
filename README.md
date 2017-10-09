# `Re.duce` 프로젝트

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
     - 메뉴 수정`
     - 할인 대상 메뉴 설정
     - 주문 내역 및 notification
   - 결제는 앱 내에서 이루어짐. `아임포트` 를 사용하여 개발할 예정

2. #### 개발 계획

   - ##### [유저] url : user/

     - `POST` ^signup/$ : 회원가입(손님, 사장님)
     - `POST` ^login/$ : 로그인
     - `GET`  ^$ : 유저 프로필 보기
     - `PATCH` ^$ : 유저 프로필 수정

   - ##### [API] base-url: api/ 서브도메인으로 빼기 고려하기 및 버전 정보 포함할 것 인지.

     ##### [손님-가게 정보] url : shops/

     - `GET` ^$?query_param=location : 가게 리스트
       - `GET` ^{shop_id}/$ : 가게 정보 받아오기
       - `GET` ^{shop_id}/menus/$?query_param=is_sale : 할인 메뉴 리스트 받아오기
         - `GET` ^{shop_id}/menus/{menu_id}/$ : 할인 메뉴 정보 받아오기

     ##### [손님-주문 정보] url : orders/

     - `POST` ^$ : 주문하기
     - `GET` ^$ : 주문 내역 리스트
       - `GET` ^{order_id}/$ : 주문 상세 내역
     - `DELETE` ^{order_id}/$ : 주문 취소

   - ##### [사장님] base-url : owner/

     ##### [사장님-가게 정보] url : my-shops/

     - `GET` ^$ : 가게 리스트 보기 
     - `POST` ^$ : 가게 등록
     - `GET` ^{shop_id}/$ : 가게 정보 보기
     - `PATCH` ^{shop_id}/$ : 가게 정보 수정
     - `DELETE` ^(shop_id)/$: 가게 삭제
     - `POST` ^{shop_id}/menus/$ : 메뉴 등록
     - `GET` ^{shop_id}/menus/?query_param=is_sale$ : 메뉴(할인) 리스트 보기
       - `GET` ^{shop_id}/menus/{menu_id}/$: 메뉴(할인) 정보 보기
     - `PATCH` ^{shop_id}/menus/{menu_id}/$ : 메뉴(할인) 정보 수정
     - `DELETE` ^{shop_id}/menus/{menu_id}/$ : 메뉴 정보 삭제

     ##### [사장님-주문 정보] url : orders/

     - `GET` ^$?query_param=shop_name : 주문 내역 리스트
       - `GET` ^{oredr_id}/$ : 주문 내역 확인
     - <u>주문 현황 알림 기능: 공부를 하자</u>

      (2단계)

   - 평점

   - 댓글

   - 팔로잉

   - 프로필

   - 재고 변동 트리거

   - 매출 정보

   - 주문 접수 확인,취소 

   - 카테고리

3. #### Reqs

   - pip install django
   - pip install djangorestframework
   - pip install drfdocs
   - Pip install django-jet
   - pip install google-api-python-client==1.4.1