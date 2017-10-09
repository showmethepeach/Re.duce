from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
from user.permissions import IsAuthenticatedOrWriteOnly

class UserManager(mixins.CreateModelMixin, generics.RetrieveUpdateAPIView):
    # UserDetailAPIView(GET, UPDATE, PUT)

    permission_classes = (IsAuthenticatedOrWriteOnly, )
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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

user_manager = UserManager.as_view()
