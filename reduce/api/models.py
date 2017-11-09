from django.db import models
from user.models import Customer
from owner.models import Shop

class Review(models.Model):
    # 리뷰 모델
    customer = models.ForeignKey(Customer) # 손님과 1:N 관계 설정
    shop = models.ForeignKey(Shop) # 가게와 1:N 관계 설정
    content = models.TextField(max_length=128) # 리뷰의 내용
    rating = models.DecimalField(max_digits=2, decimal_places=1) # 리뷰에서 가게의 별점
