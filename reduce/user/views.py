from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    # UserDetailAPIView(GET, UPDATE, PUT)

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # 유저 정보 보기(GET)
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        # 유저 정보 수정(UPDATE, PUT)
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserSignup(generics.CreateAPIView):
    # UserSignupAPIView(POST)
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # 유저 회원 가입(POST)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


user_signup = UserSignup.as_view()
user_detail = UserDetail.as_view()
