## `Re.duce` API 명세

- #### `EndPoint` : 미정

1. #### URLpath

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
       - `POST` ^{shop_id}/reviews/$ : 리뷰 등록하기
       - `GET` ^{shop_id}/reviews/$ : 리뷰 리스트 보기 
         - `GET` ^{shop_id}/reviews/{review_id}/$ : 댓글 내용 보기
         - `PUT` ^{shop_id}/reviews/{review_id}/$ : 댓글 내용 수정
         - `DELETE` ^{shop_id}/reviews/{review_id}/$ : 댓글 내용 삭제
       - `POST` ^{shop_id}/orders/$ : 주문하기
       - `GET` ^{shop_id}/orders/$ : 주문 내역 리스트
         - `GET` ^{shop_id}/orders/{order_id}/$ : 주문 상세 내역
         - `DELETE` ^{shop_id}/orders/{order_id}/$ : 주문 취소

     ​

     ##### [사장님] base-url : owner/

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
     - `GET` ^{shop_id}/reviews/$ : 리뷰 리스트 보기 
       - `GET` ^{shop_id}/reviews/{review_id}/$ : 댓글 내용 보기

     ##### [사장님-주문 정보] url : orders/

     - `GET` ^$ : 주문 내역 리스트
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

   - 마일리지(포인트)

   ​
