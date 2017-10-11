from rest_framework import serializers
from user.models import User, Customer, Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', )

class UserSerializer(serializers.ModelSerializer):

    is_owner = serializers.BooleanField(default=False, required=False,  write_only=True)
    owner = OwnerSerializer(default=None, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'phone_number', 'is_owner', 'owner')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        is_owner = validated_data.pop('is_owner', False)
        owner_data = validated_data.pop('owner', None)

        if is_owner == True:
            owner = Owner.objects.create(**owner_data)
            customer = None
        else:
            owner = None
            customer = Customer.objects.create()

        user = User(customer=customer, owner=owner, **validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            if key == 'username':
                continue
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

