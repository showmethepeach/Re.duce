from django.db import models
from django.db.models import Avg
from user.models import Customer, Owner

class Shop(models.Model):
    # 가게 모델
    owner = models.ForeignKey(Owner) # 사장님 모델과 1:N 관계 설정
    shop_id = models.IntegerField(default=0) # 각 사장님 마다 부여된 가게의 고유번호
    name = models.CharField(max_length=64) # 가게 이름
    description = models.TextField(max_length=512) # 가게 정보
    business_number = models.CharField(max_length=16, unique=True) # 사업자 등록 번호
    contact_number = models.CharField(max_length=16)# 가게 전화 번호
    address = models.CharField(max_length=64) # 가게 주소
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1) # 가게의 평점
    image = models.ImageField(upload_to='shops/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return '{}의 가게 {}'.format(self.owner.name, self.name)

    def update_rating(self):
        # 리뷰 등록 시 평점 저장
        self.rating = self.review_set.aggregate(Avg('rating'))['rating__avg']
        self.save(update_fields=['rating'])


class Menu(models.Model):
    # 메뉴 모델
    shop = models.ForeignKey(Shop) # 가게 모델과 1:N 관계 설정
    name = models.CharField(max_length=32) # 메뉴 이름
    price = models.IntegerField(default=0) # 메뉴 가격
    description = models.TextField(max_length=256) # 메뉴 정보
    is_sale = models.BooleanField(default=False) # 메뉴 할인 여부
    sale_rate = models.IntegerField(default=100) # 메뉴 할인 비율
    image = models.ImageField(upload_to='menus/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        unique_together = (('shop', 'name'),)

    def __str__(self):
        return '{}의 가게 {}의 메뉴 {}'.format(self.shop.owner, self.shop.name, self.name)

class Order(models.Model):
    # 주문 확인 모델
    # 주문 번호 필드 추가 할 것인가!!? 어떻게 번호 생성할 것인가
    customer = models.ForeignKey(Customer) # 손님 모델과 1:N 관계 설정
    shop = models.ForeignKey(Shop) # 가게 모델과 1:N 관계 설정
    is_finished = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0) # 주문 총 가격
    ordered_at = models.DateTimeField(auto_now_add=True) # 주문 일자

class OrderSaleMenu(models.Model):
    # 주문 메뉴 상세 모델
    order = models.ForeignKey(Order, related_name='order_sale_menus') # 주문 모델과 1:N 관계 설정
    menu = models.ForeignKey(Menu) # 메뉴 모델과 1:N 관계 설정
    quantity = models.IntegerField(default=1) # 메뉴 주문 개수

