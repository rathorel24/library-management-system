from .models import User

from .serializers import UserRegisterSerializer,  UserSerializer
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser


class UserViewSet(GenericViewSet,CreateModelMixin, RetrieveModelMixin):
    queryset = User.objects.filter(is_active=True)
    serializer_class =  UserSerializer
    permission_classes = (IsAuthenticated,AllowAny)

    @action(methods=["POST"],detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "register":
            return UserRegisterSerializer
        return self.serializer_class
