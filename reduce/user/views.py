from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from user.models import User
from user.serializers import UserSerializer
from user.permissions import IsAuthenticatedOrWriteOnly


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserManager(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    # 유저 관리 View

    permission_classes = (IsAuthenticatedOrWriteOnly, ) # 회원가입은 누구나 가능하게 한다.
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # 해당 요청 유저 정보 보기(GET)
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        # 해당 요청 유저 정보 수정(UPDATE, PUT)

        serializer = self.serializer_class(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

user_manager = UserManager.as_view()
