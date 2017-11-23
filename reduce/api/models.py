from django.db import models
from django.db.models.signals import post_save
from user.models import Customer
from owner.models import Shop

class Review(models.Model):
    # 리뷰 모델
    customer = models.ForeignKey(Customer) # 손님과 1:N 관계 설정
    shop = models.ForeignKey(Shop) # 가게와 1:N 관계 설정
    content = models.TextField(max_length=128) # 리뷰의 내용
    rating = models.DecimalField(max_digits=2, decimal_places=1) # 리뷰에서 가게의 별점

    def on_post_save(sender, **kwargs):
        # 리뷰 작성시 실행
        review = kwargs['instance']
        if kwargs['created']:
            #지금 생성된게 맞다면
            review.shop.update_rating()

post_save.connect(Review.on_post_save, sender=Review)
