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
     - 메뉴 수정
     - 할인 대상 메뉴 설정
     - 주문 내역 및 notification
   - 결제는 앱 내에서 이루어짐. `아임포트` 를 사용하여 개발할 예정

2. #### Reqs

   - pip install django
   - pip install djangorestframework
   - pip install drfdocs
   - Pip install django-jet
   - pip install google-api-python-client==1.4.1