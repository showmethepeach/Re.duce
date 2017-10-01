from django.db import models
from django.contrib.auth.models import AbstractUser

class Owner(models.Model):
    # 사장님 유저 모델
    name = models.CharField(max_length=32) # 사장님 이름

    def __str__(self):
        return self.name

class Customer(models.Model):
    # 손님 유저 모델
    pass

class User(AbstractUser):
    # 기본 유저 확장 모델
    phone_number = models.CharField(max_length=16) # 핸드폰 번호
    owner = models.OneToOneField(Owner, blank=True, null=True, related_name='user_owner') # 사장님 모델을 통한 확장
    customer = models.OneToOneField(Customer, blank=True, null=True, related_name='user_customer') # 손님 모델을 통한 확장

    def __str__(self):
        return self.username
