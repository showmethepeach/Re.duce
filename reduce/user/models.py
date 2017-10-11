from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
class Owner(models.Model):
    # 사장님 유저 모델

    name = models.CharField(max_length=32) # 사장님 이름

    def __str__(self):
        try:
            # Owner따로 생성 시 user model과 연결이 안되어 있어 ObjectDoesNotExist에러 발생
            return 'id: {}, 이름: {}'.format(self.user.username, self.name)
        except ObjectDoesNotExist:
            return 'Owner'

class Customer(models.Model):
    # 손님 유저 모델

    def __str__(self):
        try:
            # customer따로 생성 시 user model과 연결이 안되어 있어 ObjectDoesNotExist에러 발생
            return self.user.username
        except ObjectDoesNotExist:
            return 'Customer'

class User(AbstractUser):
    # 기본 유저 확장 모델
    phone_number = models.CharField(max_length=16) # 핸드폰 번호
    owner = models.OneToOneField(Owner, blank=True, null=True) # 사장님 모델을 통한 확장
    customer = models.OneToOneField(Customer, blank=True, null=True) # 손님 모델을 통한 확장

    def __str__(self):
        return self.username
